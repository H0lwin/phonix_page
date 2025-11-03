"""
WSGI config for cms_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path
import django
from django.core.wsgi import get_wsgi_application

# Add the project directory to Python path
project_dir = '/var/www/phonix-page'
sys.path.append(project_dir)
sys.path.append(os.path.join(project_dir, 'cms_project'))

# Load environment variables from .env file if it exists
env_file = Path(project_dir) / '.env'
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ.setdefault(key, value)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms_project.settings')

try:
    django.setup()
    application = get_wsgi_application()
except Exception:
    # Error loading the application
    import traceback
    traceback.print_exc()
    raise