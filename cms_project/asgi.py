"""
ASGI config for cms_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import sys
from django.core.asgi import get_asgi_application

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms_project.settings')

try:
    application = get_asgi_application()
except Exception:
    # Error loading the application
    import traceback
    traceback.print_exc()
    raise