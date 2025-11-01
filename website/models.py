from django.db import models
from django.core.exceptions import ValidationError

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError("Only one instance of this model is allowed.")
        return super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SiteSettings(SingletonModel):
    # Basic site information
    site_name = models.CharField(max_length=100, default="شهر راز")
    site_title = models.CharField(max_length=200, default="راه‌حل جامع برای تمام نیازهای مالی و حقوقی شما")
    site_description = models.TextField(default="شهر راز با بیش از ۱۵ سال تجربه، ارائه‌دهنده خدمات تخصصی خرید و فروش وام، لیزینگ خودرو، ثبت شرکت، خدمات حقوقی و قضایی، ثبت مجوزها و کارت‌های بازرگانی است.")
    
    # Hero section
    hero_badge = models.CharField(max_length=100, default="✨ مرکز تخصصی خدمات مالی و حقوقی")
    hero_subtitle = models.TextField(default="شهر راز با بیش از ۱۵ سال تجربه، ارائه‌دهنده خدمات تخصصی خرید و فروش وام، لیزینگ خودرو، ثبت شرکت، خدمات حقوقی و قضایی، ثبت مجوزها و کارت‌های بازرگانی است. ما با تیم متخصص و سیستم‌های پیشرفته، بهترین راه‌حل را برای شما فراهم می‌کنیم.")
    
    # Services section
    services_title = models.CharField(max_length=100, default="خدمات تخصصی ما")
    services_subtitle = models.CharField(max_length=200, default="مجموعه کامل خدمات مالی و حقوقی در یک مکان")
    
    # Service items
    service_loan_title = models.CharField(max_length=100, default="خرید و فروش وام")
    service_loan_description = models.TextField(default="خرید و فروش انواع وام‌های بانکی با بهترین نرخ و شرایط. ما واسطه معتبر بین خریداران و فروشندگان وام هستیم.")
    
    service_leasing_title = models.CharField(max_length=100, default="لیزینگ خودرو")
    service_leasing_description = models.TextField(default="ارائه خدمات لیزینگ خودرو با شرایط ویژه و اقساط مناسب. خرید خودرو بدون دغدغه مالی با لیزینگ شهر راز.")
    
    service_registration_title = models.CharField(max_length=100, default="ثبت شرکت")
    service_registration_description = models.TextField(default="ثبت انواع شرکت‌ها شامل سهامی خاص، با مسئولیت محدود، تعاونی و... با سرعت و دقت بالا.")
    
    service_legal_title = models.CharField(max_length=100, default="خدمات حقوقی و قضایی")
    service_legal_description = models.TextField(default="ارائه مشاوره حقوقی، وکالت در دادگاه‌ها، تنظیم قراردادها و پیگیری امور قضایی توسط وکلای مجرب.")
    
    service_licenses_title = models.CharField(max_length=100, default="ثبت مجوزها")
    service_licenses_description = models.TextField(default="اخذ و ثبت انواع مجوزهای کسب‌وکار، پروانه‌های صنفی، مجوزهای بهداشتی و صنعتی.")
    
    service_commercial_title = models.CharField(max_length=100, default="کارت بازرگانی")
    service_commercial_description = models.TextField(default="اخذ و تمدید کارت بازرگانی، ثبت کدهای اقتصادی و انجام امور مربوط به واردات و صادرات.")
    
    # Features section
    features_title = models.CharField(max_length=100, default="چرا شهر راز؟")
    features_subtitle = models.CharField(max_length=200, default="دلایلی که ما را متمایز می‌کند")
    
    # Footer information
    footer_company_name = models.CharField(max_length=100, default="شهر راز")
    footer_company_description = models.TextField(default="شرکت خدمات حقوقی تخصصی با بیش از ۱۵ سال تجربه در ارائه بهترین خدمات حقوقی")
    footer_address_title = models.CharField(max_length=100, default="آدرس دفتر")
    footer_address = models.TextField(default="تهران، خیابان آزادی، پلاک ۱۲۳\nطبقه ۵، واحد ۱۰")
    footer_hours_title = models.CharField(max_length=100, default="ساعات کاری")
    footer_hours = models.TextField(default="شنبه تا چهارشنبه: ۹ صبح تا ۶ عصر\nپنجشنبه: ۹ صبح تا ۱ ظهر")
    
    # Contact information
    contact_phone_title = models.CharField(max_length=100, default="تماس با ما")
    contact_phone = models.CharField(max_length=100, default="۰۲۱-۱۲۳۴۵۶۷۸")
    
    # Trust section
    trust_title = models.CharField(max_length=100, default="چرا به ما اعتماد کنید؟")
    trust_subtitle = models.CharField(max_length=200, default="آمار و ارقام گویای کیفیت خدمات ما")
    
    # FAQ section
    faq_title = models.CharField(max_length=100, default="سوالات متداول")
    faq_subtitle = models.CharField(max_length=200, default="پاسخ به سوالات رایج شما")
    
    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"