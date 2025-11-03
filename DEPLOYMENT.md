# Django CMS Deployment Guide

This guide provides instructions for deploying the Shahr-e Raze CMS application in a production environment using WSGI.

## Prerequisites

- Python 3.8 or higher
- A WSGI server (Gunicorn, uWSGI, or Apache with mod_wsgi)
- A web server (Nginx or Apache)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd cms
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

## WSGI Deployment

### Using Gunicorn (Recommended)

1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Run the application:
   ```bash
   gunicorn --bind 0.0.0.0:8000 cms_project.wsgi:application
   ```

### Using uWSGI

1. Install uWSGI:
   ```bash
   pip install uwsgi
   ```

2. Create a uwsgi.ini file:
   ```ini
   [uwsgi]
   module = cms_project.wsgi:application
   master = true
   processes = 4
   socket = :8000
   chmod-socket = 666
   vacuum = true
   die-on-term = true
   ```

3. Run the application:
   ```bash
   uwsgi --ini uwsgi.ini
   ```

## Web Server Configuration

### Nginx Configuration

Create an Nginx configuration file (e.g., `/etc/nginx/sites-available/cms`):

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /static/ {
        alias /path/to/your/project/static/;
    }

    location /media/ {
        alias /path/to/your/project/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/cms /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## Environment Variables

Set the following environment variables in production:

```bash
export DJANGO_SETTINGS_MODULE=cms_project.settings
export SECRET_KEY="your-secret-key"
export DEBUG=False
export ALLOWED_HOSTS="your-domain.com,www.your-domain.com"
```

## Security Considerations

1. Always set `DEBUG=False` in production
2. Use a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS` properly
4. Serve static files through the web server, not Django
5. Use HTTPS in production
6. Regularly update dependencies

## Database Configuration

For production, consider using PostgreSQL or MySQL instead of SQLite:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Monitoring and Logging

Configure logging in your Django settings:

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/path/to/your/log/file.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```