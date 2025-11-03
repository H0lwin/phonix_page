"""
WSGI config for cms_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add the project directory to Python path
sys.path.append('/var/www/phonix-page')
sys.path.append('/var/www/phonix-page/cms_project')

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