from django.contrib import admin
from .models import (
    SiteSettings, HeroSection, Statistic, Service, LoanCategory, LoanItem,
    LeasingOffer, Category, ServiceItem, WhyUsFeature, Comparison, Testimonial,
    FAQ, ContactInfo, CollaborationProcess, CollaborationStep, Company
)

# 1. SiteSettings Admin
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name',)
    fieldsets = (
        ('اطلاعات عمومی', {
            'fields': ('site_name', 'description', 'footer_text')
        }),
        ('اطلاعات تماس', {
            'fields': ('phone_main', 'phone_alt', 'email_main', 'email_support', 'work_hours')
        }),
        ('آدرس‌ها', {
            'fields': ('head_office_address', 'branch_office_address')
        }),
        ('سئو', {
            'fields': ('meta_keywords', 'meta_description'),
        }),
        ('رسانه', {
            'fields': ('logo', 'favicon'),
        }),
    )
    verbose_name = "تنظیمات سایت"
    verbose_name_plural = "تنظیمات سایت"

# 2. HeroSection Admin
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('headline', 'cta_primary_text', 'cta_secondary_text')
    fieldsets = (
        ('محتوا', {
            'fields': ('headline', 'subheadline')
        }),
        ('دکمه‌ها', {
            'fields': ('cta_primary_text', 'cta_primary_link', 'cta_secondary_text', 'cta_secondary_link')
        }),
        ('رسانه', {
            'fields': ('background_image',)
        }),
    )
    verbose_name = "بخش هرو"
    verbose_name_plural = "بخش هرو"

# 3. Statistic Admin
@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'icon', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    verbose_name = "آمار"
    verbose_name_plural = "آمارها"

# 4. Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)
    verbose_name = "خدمات"
    verbose_name_plural = "خدمات"

# 5. LoanCategory and LoanItem Admin
@admin.register(LoanCategory)
class LoanCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    verbose_name = "دسته‌بندی وام"
    verbose_name_plural = "دسته‌بندی وام‌ها"

@admin.register(LoanItem)
class LoanItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'is_active')
    list_filter = ('category', 'is_active')
    verbose_name = "آیتم وام"
    verbose_name_plural = "آیتم‌های وام"

# 6. LeasingOffer Admin
@admin.register(LeasingOffer)
class LeasingOfferAdmin(admin.ModelAdmin):
    list_display = ('title',)
    verbose_name = "پیشنهاد لیزینگ"
    verbose_name_plural = "پیشنهادات لیزینگ"

# 7. Category and ServiceItem Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    verbose_name = "دسته‌بندی"
    verbose_name_plural = "دسته‌بندی‌ها"

@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'cta_text')
    list_filter = ('category',)
    verbose_name = "آیتم خدمات"
    verbose_name_plural = "آیتم‌های خدمات"

# 8. WhyUsFeature Admin
@admin.register(WhyUsFeature)
class WhyUsFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    verbose_name = "ویژگی ما"
    verbose_name_plural = "ویژگی‌های ما"

# 9. Comparison Admin
@admin.register(Comparison)
class ComparisonAdmin(admin.ModelAdmin):
    list_display = ('criterion', 'our_value', 'others_value')
    verbose_name = "مقایسه"
    verbose_name_plural = "مقایسه‌ها"

# 10. Testimonial Admin
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_role', 'rating', 'status')
    list_filter = ('rating', 'status')
    verbose_name = "نظر مشتری"
    verbose_name_plural = "نظرات مشتریان"

# 11. FAQ Admin
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)
    verbose_name = "سؤال متداول"
    verbose_name_plural = "سؤالات متداول"

# 12. ContactInfo Admin
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')
    verbose_name = "اطلاعات تماس"
    verbose_name_plural = "اطلاعات تماس"


# 13. Collaboration Process Admin
class CollaborationStepInline(admin.TabularInline):
    model = CollaborationStep
    extra = 1
    fields = ('title', 'description', 'order', 'icon')
    ordering = ('order',)


@admin.register(CollaborationProcess)
class CollaborationProcessAdmin(admin.ModelAdmin):
    list_display = ('title', 'cta_text')
    inlines = [CollaborationStepInline]
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'description')
        }),
        ('دکمه اقدام', {
            'fields': ('cta_text', 'cta_link')
        }),
    )
    verbose_name = "بخش فرآیند همکاری"
    verbose_name_plural = "بخش‌های فرآیند همکاری"


@admin.register(CollaborationStep)
class CollaborationStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'process', 'order', 'icon')
    list_filter = ('process',)
    ordering = ('process', 'order')
    search_fields = ('title', 'description')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)
    search_fields = ('name',)
    verbose_name = "شرکت"
    verbose_name_plural = "شرکت‌ها"