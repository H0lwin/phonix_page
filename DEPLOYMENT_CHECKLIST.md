# Deployment Checklist for Shahr-e Raze CMS

## Pre-deployment Tasks

- [ ] Update `settings.py` with production values:
  - [ ] Set `DEBUG = False`
  - [ ] Update `ALLOWED_HOSTS` with your domain
  - [ ] Set proper `SECRET_KEY`
  - [ ] Configure database settings for production (PostgreSQL recommended)
  
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

## Environment Variables

- [ ] Set environment variables:
  ```bash
  export SECRET_KEY="your-secret-key"
  export DEBUG=False
  export ALLOWED_HOSTS="localhost,127.0.0.1,citysecret.ir,www.citysecret.ir"
  ```
  
- [ ] Or create a .env file with the variables:
  ```
  SECRET_KEY=your-secret-key
  DEBUG=False
  ALLOWED_HOSTS=localhost,127.0.0.1,citysecret.ir,www.citysecret.ir
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