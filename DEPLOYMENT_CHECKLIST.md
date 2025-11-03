# Deployment Checklist for Shahr-e Raze CMS

## Pre-deployment Tasks

- [ ] Update `settings.py` with production values:
  - [ ] Set `DEBUG = False`
  - [ ] Update `ALLOWED_HOSTS` with your domain
  - [ ] Set proper `SECRET_KEY`
  - [ ] Configure database settings for production (MySQL recommended)
  
- [ ] Collect static files:
  ```bash
  python manage.py collectstatic --noinput
  ```

- [ ] Run migrations:
  ```bash
  python manage.py migrate
  ```

- [ ] Create superuser:
  ```bash
  python manage.py createsuperuser
  ```

## Database Setup (MySQL)

- [ ] Install MySQL server and client:
  ```bash
  sudo apt update
  sudo apt install mysql-server mysql-client libmysqlclient-dev
  ```

- [ ] Start MySQL service:
  ```bash
  sudo systemctl start mysql
  sudo systemctl enable mysql
  ```

- [ ] Secure MySQL installation:
  ```bash
  sudo mysql_secure_installation
  ```

- [ ] Create database and user:
  ```sql
  CREATE DATABASE shahreraze_cms_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  CREATE USER 'shahreraze_cms_user'@'localhost' IDENTIFIED BY 'your_strong_password';
  GRANT ALL PRIVILEGES ON shahreraze_cms_db.* TO 'shahreraze_cms_user'@'localhost';
  FLUSH PRIVILEGES;
  ```

## Environment Variables Setup

- [ ] Create a `.env` file in the project root directory:
  ```bash
  touch .env
  ```

- [ ] Generate a secure secret key:
  ```bash
  python generate_secret_key.py
  ```

- [ ] Add the following variables to your `.env` file:
  ```
  # Django Security Settings
  SECRET_KEY=your-generated-secret-key-here
  DEBUG=False
  
  # Host Settings
  ALLOWED_HOSTS=localhost,127.0.0.1,citysecret.ir,www.citysecret.ir
  
  # Database Settings
  DB_NAME=shahreraze_cms_db
  DB_USER=shahreraze_cms_user
  DB_PASSWORD=your_strong_password
  DB_HOST=localhost
  DB_PORT=3306
  
  # Path Settings
  STATIC_ROOT=/var/www/phonix-page/static
  MEDIA_ROOT=/var/www/phonix-page/media
  
  # Additional Security Settings
  SECURE_SSL_REDIRECT=True
  SESSION_COOKIE_SECURE=True
  CSRF_COOKIE_SECURE=True
  ```

## Migration Fix for MySQL Row Size Issue

If you encounter a "Row size too large" error when migrating to MySQL, follow these steps:

1. The project includes custom migrations (0011 and 0012) that address this issue by breaking down the large migration into smaller parts.

2. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

## Handling Duplicate Column Errors

If you encounter a "Duplicate column name" error:

1. This happens when some fields were already added to the database but Django's migration tracking is out of sync.

2. The project includes migration 0013 that handles this issue by checking for existing columns before adding them.

3. If the error persists, you can reset the migration state:
   ```bash
   # Backup your database first
   mysqldump -u shahreraze_cms_user -p shahreraze_cms_db > backup.sql
   
   # Remove migration records for the website app
   mysql -u shahreraze_cms_user -p shahreraze_cms_db -e "DELETE FROM django_migrations WHERE app = 'website';"
   
   # Run migrations again
   python manage.py migrate
   ```

## Server Configuration

- [ ] Install required packages:
  ```bash
  sudo apt update
  sudo apt install apache2 libapache2-mod-wsgi-py3 python3-dev python3-pip
  ```

- [ ] Create project directory:
  ```bash
  sudo mkdir -p /var/www/phonix-page
  ```

- [ ] Set proper permissions:
  ```bash
  sudo chown -R www-data:www-data /var/www/phonix-page
  sudo chmod -R 755 /var/www/phonix-page
  ```

- [ ] Upload project files to server

- [ ] Create virtual environment:
  ```bash
  cd /var/www/phonix-page
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

## Apache Configuration

- [ ] Copy Apache configuration:
  ```bash
  sudo cp apache_config.conf /etc/apache2/sites-available/citysecret.ir.conf
  ```

- [ ] Enable site:
  ```bash
  sudo a2ensite citysecret.ir.conf
  ```

- [ ] Enable required modules:
  ```bash
  sudo a2enmod ssl rewrite headers proxy proxy_http wsgi
  ```

- [ ] Test Apache configuration:
  ```bash
  sudo apache2ctl configtest
  ```

- [ ] Restart Apache:
  ```bash
  sudo systemctl restart apache2
  ```

## Post-deployment Tasks

- [ ] Verify site is accessible
- [ ] Test admin panel
- [ ] Check static files are served correctly
- [ ] Test all forms and functionality
- [ ] Verify SSL certificate is working
- [ ] Check error logs for any issues

## Security Considerations

- [ ] Ensure proper file permissions
- [ ] Verify database security
- [ ] Check SSL certificate validity
- [ ] Review firewall settings
- [ ] Set up regular backups
- [ ] Monitor logs for suspicious activity

## Monitoring

- [ ] Set up log rotation
- [ ] Configure monitoring alerts
- [ ] Test backup restoration
- [ ] Document deployment process