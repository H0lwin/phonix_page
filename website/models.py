from django.db import models
from django.utils import timezone

# 1. SiteSettings (general site settings)
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, verbose_name="نام سایت", default="شهر راز")
    description = models.TextField(verbose_name="توضیحات", default="خدمات مالی و حقوقی تخصصی")
    address = models.TextField(verbose_name="آدرس", default="تهران، ایران")
    phone_main = models.CharField(max_length=20, verbose_name="تلفن اصلی", default="021-1234-5678")
    phone_alt = models.CharField(max_length=20, blank=True, verbose_name="تلفن جایگزین", default="")
    email_main = models.EmailField(verbose_name="ایمیل اصلی", default="info@shahreraze.com")
    email_support = models.EmailField(verbose_name="ایمیل پشتیبانی", default="support@shahreraze.com")
    work_hours = models.CharField(max_length=100, verbose_name="ساعات کاری", default="شنبه-پنجشنبه: 9صبح-6عصر")
    logo = models.ImageField(upload_to='logos/', blank=True, verbose_name="لوگو")
    favicon = models.ImageField(upload_to='favicons/', blank=True, verbose_name="آیکون")
    meta_keywords = models.TextField(blank=True, verbose_name="کلمات کلیدی متا", default="")
    meta_description = models.TextField(blank=True, verbose_name="توضیحات متا", default="")
    footer_text = models.TextField(verbose_name="متن فوتر", default="© 2025 شهر راز. تمامی حقوق محفوظ است.")
    
    # Additional address fields for multiple office locations
    head_office_address = models.TextField(verbose_name="آدرس دفتر مرکزی", default="تهران، خیابان آزادی، پلاک ۱۲۳")
    branch_office_address = models.TextField(verbose_name="آدرس شعبه", blank=True, default="")
    
    def __str__(self):
        return str(self.site_name)
    
    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

# 2. HeroSection (header or main introduction section)
class HeroSection(models.Model):
    headline = models.CharField(max_length=200, verbose_name="عنوان", default="خدمات مالی و حقوقی جامع")
    subheadline = models.TextField(verbose_name="زیرعنوان", default="خدمات حرفه‌ای برای تمام نیازهای مالی و حقوقی شما")
    cta_primary_text = models.CharField(max_length=100, verbose_name="متن دکمه اصلی", default="تماس با ما")
    cta_primary_link = models.URLField(verbose_name="لینک دکمه اصلی", default="#contact")
    cta_secondary_text = models.CharField(max_length=100, verbose_name="متن دکمه ثانویه", default="مشاهده خدمات")
    cta_secondary_link = models.URLField(verbose_name="لینک دکمه ثانویه", default="#services")
    background_image = models.ImageField(upload_to='hero/', blank=True, verbose_name="تصویر پس‌زمینه")
    
    def __str__(self):
        return str(self.headline)
    
    class Meta:
        verbose_name = "بخش هرو"
        verbose_name_plural = "بخش هرو"

# 3. Statistic (Statistics and indicators)
class Statistic(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان", default="مشتریان")
    value = models.IntegerField(verbose_name="مقدار", default=100)
    icon = models.CharField(max_length=50, verbose_name="آیکون", default="👥")
    order = models.PositiveIntegerField(verbose_name="ترتیب", default=0)
    
    def __str__(self):
        return f"{self.title}: {self.value}"
    
    class Meta:
        ordering = ['order']
        verbose_name = "آمار"
        verbose_name_plural = "آمارها"

# 4. Service (Our specialized services)
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان", default="خدمات")
    icon = models.CharField(max_length=50, verbose_name="آیکون", default="🔧")
    short_description = models.TextField(verbose_name="توضیحات کوتاه", default="توضیحات خدمات")
    content = models.TextField(verbose_name="محتوا", default="محتوای کامل خدمات")  # Using TextField instead of RichTextField for simplicity
    order = models.PositiveIntegerField(verbose_name="ترتیب", default=0)
    is_active = models.BooleanField(verbose_name="فعال", default=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['order']
        verbose_name = "خدمات"
        verbose_name_plural = "خدمات"

# 5. LoanCategory (Loan Classification)
class LoanCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان", default="دسته‌بندی وام")
    icon = models.CharField(max_length=50, verbose_name="آیکون", default="💰")
    description = models.TextField(verbose_name="توضیحات", default="توضیحات دسته‌بندی وام")
    order = models.PositiveIntegerField(verbose_name="ترتیب", default=0)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['order']
        verbose_name = "دسته‌بندی وام"
        verbose_name_plural = "دسته‌بندی وام‌ها"

class LoanItem(models.Model):
    category = models.ForeignKey(LoanCategory, on_delete=models.CASCADE, verbose_name="دسته‌بندی")
    title = models.CharField(max_length=100, verbose_name="عنوان", default="آیتم وام")
    description = models.TextField(verbose_name="توضیحات", default="توضیحات آیتم وام")
    is_active = models.BooleanField(verbose_name="فعال", default=True)
    
    def __str__(self):
        return f"{self.category} - {self.title}"
    
    class Meta:
        verbose_name = "آیتم وام"
        verbose_name_plural = "آیتم‌های وام"

# 6. LeasingOffer (Car Leasing)
class LeasingOffer(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان", default="لیزینگ خودرو")
    description = models.TextField(verbose_name="توضیحات", default="توضیحات پیشنهاد لیزینگ")
    features = models.TextField(help_text="هر ویژگی را در یک خط وارد کنید", verbose_name="ویژگی‌ها", default="ویژگی 1\nویژگی 2\nویژگی 3")
    stats = models.TextField(help_text="آمارها را به فرمت: برچسب:مقدار (در هر خط یکی) وارد کنید", verbose_name="آمارها", default="قیمت:10000\nمدت:24 ماه")
    
    def __str__(self):
        return str(self.title)
    
    def get_stats_list(self):
        """
        Parse the stats field and return a list of dictionaries with label and value
        """
        stats_list = []
        if self.stats:
            for line in self.stats.splitlines():
                if ':' in line:
                    label, value = line.split(':', 1)
                    stats_list.append({
                        'label': label.strip(),
                        'value': value.strip()
                    })
        return stats_list
    
    class Meta:
        verbose_name = "پیشنهاد لیزینگ"
        verbose_name_plural = "پیشنهادات لیزینگ"

# 7. CompanyRegistration (Registration and License Services)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام", default="دسته‌بندی")
    icon = models.CharField(max_length=50, verbose_name="آیکون", default="📂")
    description = models.TextField(verbose_name="توضیحات", default="توضیحات دسته‌بندی")
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

class ServiceItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته‌بندی")
    title = models.CharField(max_length=100, verbose_name="عنوان", default="آیتم خدمات")
    description = models.TextField(verbose_name="توضیحات", default="توضیحات آیتم خدمات")
    cta_text = models.CharField(max_length=100, verbose_name="متن دکمه عملیات", default="اطلاعات بیشتر")
    cta_link = models.URLField(verbose_name="لینک دکمه عملیات", default="#")
    
    def __str__(self):
        return f"{self.category} - {self.title}"
    
    class Meta:
        verbose_name = "آیتم خدمات"
        verbose_name_plural = "آیتم‌های خدمات"

# 8. WhyUsFeature (Benefits and reasons to trust)
class WhyUsFeature(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان", default="ویژگی")
    icon = models.CharField(max_length=50, verbose_name="آیکون", default="⭐")
    description = models.TextField(verbose_name="توضیحات", default="توضیحات ویژگی")
    order = models.PositiveIntegerField(verbose_name="ترتیب", default=0)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['order']
        verbose_name = "ویژگی ما"
        verbose_name_plural = "ویژگی‌های ما"

# 9. Comparison
class Comparison(models.Model):
    criterion = models.CharField(max_length=100, verbose_name="معیار", default="معیار")
    our_value = models.CharField(max_length=100, verbose_name="مقدار ما", default="مقدار ما")
    others_value = models.CharField(max_length=100, verbose_name="مقدار دیگران", default="مقدار دیگران")
    
    def __str__(self):
        return str(self.criterion)
    
    class Meta:
        verbose_name = "مقایسه"
        verbose_name_plural = "مقایسه‌ها"

# 10. Testimonial with status field
class Testimonial(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در حال بررسی'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    ]
    
    client_name = models.CharField(max_length=100, verbose_name="نام مشتری", default="مشتری")
    client_role = models.CharField(max_length=100, verbose_name="نقش مشتری", default="نقش مشتری")
    comment = models.TextField(verbose_name="نظر", default="نظر مشتری")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="امتیاز", default=5)
    photo = models.ImageField(upload_to='testimonials/', blank=True, verbose_name="تصویر")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="وضعیت")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ایجاد")
    
    def __str__(self):
        return f"{self.client_name} - {self.rating} ستاره"
    
    class Meta:
        verbose_name = "نظر مشتری"
        verbose_name_plural = "نظرات مشتریان"

# 11. FAQ (Frequently Asked Questions)
class FAQ(models.Model):
    question = models.CharField(max_length=200, verbose_name="سؤال", default="سؤال")
    answer = models.TextField(verbose_name="پاسخ", default="پاسخ")
    order = models.PositiveIntegerField(verbose_name="ترتیب", default=0)
    is_active = models.BooleanField(verbose_name="فعال", default=True)
    
    def __str__(self):
        return str(self.question)
    
    class Meta:
        ordering = ['order']
        verbose_name = "سؤال متداول"
        verbose_name_plural = "سؤالات متداول"

# 12. ContactInfo
class ContactInfo(models.Model):
    phone = models.CharField(max_length=20, verbose_name="تلفن", default="021-1234-5678")
    email = models.EmailField(verbose_name="ایمیل", default="info@shahreraze.com")
    address = models.TextField(verbose_name="آدرس", default="تهران، ایران")
    map_embed = models.TextField(blank=True, verbose_name="کد نقشه", default="")
    
    def __str__(self):
        return f"اطلاعات تماس - {self.phone}"
    
    class Meta:
        verbose_name = "اطلاعات تماس"
        verbose_name_plural = "اطلاعات تماس"