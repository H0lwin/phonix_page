from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name',)
    
    fieldsets = (
        ('Site Information', {
            'fields': ('site_name', 'site_title', 'site_description')
        }),
        ('Hero Section', {
            'fields': ('hero_badge', 'hero_subtitle')
        }),
        ('Services Section', {
            'fields': ('services_title', 'services_subtitle')
        }),
        ('Service Items', {
            'fields': (
                'service_loan_title', 'service_loan_description',
                'service_leasing_title', 'service_leasing_description',
                'service_registration_title', 'service_registration_description',
                'service_legal_title', 'service_legal_description',
                'service_licenses_title', 'service_licenses_description',
                'service_commercial_title', 'service_commercial_description'
            )
        }),
        ('Features Section', {
            'fields': ('features_title', 'features_subtitle')
        }),
        ('Footer Information', {
            'fields': (
                'footer_company_name', 'footer_company_description',
                'footer_address_title', 'footer_address',
                'footer_hours_title', 'footer_hours',
                'contact_phone_title', 'contact_phone'
            )
        }),
        ('Trust Section', {
            'fields': ('trust_title', 'trust_subtitle')
        }),
        ('FAQ Section', {
            'fields': ('faq_title', 'faq_subtitle')
        }),
    )
    
    def has_add_permission(self, request):
        # Allow adding only if no instances exist
        return not SiteSettings.objects.exists()