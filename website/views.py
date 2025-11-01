from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import SiteSettings

def index(request):
    # Get the site settings instance (there should be only one)
    try:
        site_settings = SiteSettings.load()
    except ObjectDoesNotExist:
        # If no settings exist, create a default one
        site_settings = SiteSettings()
        site_settings.save()
    
    context = {
        'site_settings': site_settings,
    }
    
    return render(request, 'index.html', context)