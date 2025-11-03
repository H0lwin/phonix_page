from django.core.management.base import BaseCommand
from website.models import (
    SiteSettings, HeroSection, Statistic, Service, LoanCategory, LoanItem,
    LeasingOffer, Category, ServiceItem, WhyUsFeature, Comparison, Testimonial,
    FAQ, ContactInfo
)

class Command(BaseCommand):
    help = 'Initialize the site with default Persian content'

    def handle(self, *args, **options):
        # Create or update SiteSettings
        site_settings, created = SiteSettings.objects.get_or_create(
            id=1,
            defaults={
                'site_name': 'شهر راز',
                'description': 'مرکز تخصصی خرید و فروش وام، لیزینگ خودرو، ثبت شرکت و خدمات حقوقی',
                'address': 'تهران، خیابان آزادی، پلاک ۱۲۳\nطبقه ۵، واحد ۱۰',
                'phone_main': '021-1234-5678',
                'phone_alt': '0912-345-6789',
                'email_main': 'info@shahrar.ir',
                'email_support': 'support@shahrar.ir',
                'work_hours': 'شنبه تا چهارشنبه: ۹ صبح تا ۶ عصر\nپنجشنبه: ۹ صبح تا ۱ ظهر',
                'meta_keywords': 'خرید وام, فروش وام, لیزینگ خودرو, ثبت شرکت, خدمات حقوقی, وکالت, ثبت مجوز',
                'meta_description': 'شهر راز - مرکز تخصصی خدمات مالی و حقوقی با بیش از ۱۵ سال تجربه',
                'footer_text': 'شرکت خدمات حقوقی تخصصی با بیش از ۱۵ سال تجربه در ارائه بهترین خدمات حقوقی'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created SiteSettings'))
        else:
            self.stdout.write(self.style.SUCCESS('SiteSettings already exists'))

        # Create or update HeroSection
        hero, created = HeroSection.objects.get_or_create(
            id=1,
            defaults={
                'headline': 'راه‌حل جامع برای تمام نیازهای مالی و حقوقی شما',
                'subheadline': 'شهر راز با بیش از ۱۵ سال تجربه، ارائه‌دهنده خدمات تخصصی خرید و فروش وام، لیزینگ خودرو، ثبت شرکت، خدمات حقوقی و قضایی، ثبت مجوزها و کارت‌های بازرگانی است. ما با تیم متخصص و سیستم‌های پیشرفته، بهترین راه‌حل را برای شما فراهم می‌کنیم.',
                'cta_primary_text': 'مشاهده خدمات',
                'cta_primary_link': '#services',
                'cta_secondary_text': 'مشاوره رایگان',
                'cta_secondary_link': '#contact'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created HeroSection'))
        else:
            self.stdout.write(self.style.SUCCESS('HeroSection already exists'))

        # Create Statistics
        stats_data = [
            {'title': 'مشتری راضی', 'value': 2000, 'icon': '👥', 'order': 1},
            {'title': 'متخصص حرفه‌ای', 'value': 50, 'icon': '💼', 'order': 2},
            {'title': 'سال تجربه', 'value': 15, 'icon': '🏆', 'order': 3},
        ]
        
        for stat_data in stats_data:
            stat, created = Statistic.objects.get_or_create(
                title=stat_data['title'],
                defaults=stat_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created Statistic: {stat.title}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Statistic already exists: {stat.title}'))

        # Create Services
        services_data = [
            {
                'title': 'خرید و فروش وام',
                'icon': '💰',
                'short_description': 'خرید و فروش انواع وام‌های بانکی با بهترین نرخ و شرایط. ما واسطه معتبر بین خریداران و فروشندگان وام هستیم.',
                'content': 'خدمات تخصصی خرید و فروش انواع وام‌های بانکی با بهترین نرخ و شرایط. ما واسطه معتبر بین خریداران و فروشندگان وام هستیم و تمام مراحل را با دقت و شفافیت انجام می‌دهیم.',
                'order': 1,
                'is_active': True
            },
            {
                'title': 'لیزینگ خودرو',
                'icon': '🚗',
                'short_description': 'ارائه خدمات لیزینگ خودرو با شرایط ویژه و اقساط مناسب. خرید خودرو بدون دغدغه مالی با لیزینگ شهر راز.',
                'content': 'ارائه خدمات لیزینگ خودرو با شرایط ویژه و اقساط مناسب. خرید خودرو بدون دغدغه مالی با لیزینگ شهر راز و بدون نیاز به وثیقه سنگین.',
                'order': 2,
                'is_active': True
            },
            {
                'title': 'ثبت شرکت',
                'icon': '🏢',
                'short_description': 'ثبت انواع شرکت‌ها شامل سهامی خاص، با مسئولیت محدود، تعاونی و... با سرعت و دقت بالا.',
                'content': 'ثبت انواع شرکت‌ها شامل سهامی خاص، با مسئولیت محدود، تعاونی و... با سرعت و دقت بالا. تیم متخصص ما تمام مراحل را به سرعت و با رعایت کامل قوانین انجام می‌دهد.',
                'order': 3,
                'is_active': True
            },
            {
                'title': 'خدمات حقوقی و قضایی',
                'icon': '⚖️',
                'short_description': 'ارائه مشاوره حقوقی، وکالت در دادگاه‌ها، تنظیم قراردادها و پیگیری امور قضایی توسط وکلای مجرب.',
                'content': 'ارائه مشاوره حقوقی، وکالت در دادگاه‌ها، تنظیم قراردادها و پیگیری امور قضایی توسط وکلای مجرب. خدمات حقوقی جامع برای افراد و شرکت‌ها.',
                'order': 4,
                'is_active': True
            },
            {
                'title': 'ثبت مجوزها',
                'icon': '📜',
                'short_description': 'اخذ و ثبت انواع مجوزهای کسب‌وکار، پروانه‌های صنفی، مجوزهای بهداشتی و صنعتی.',
                'content': 'اخذ و ثبت انواع مجوزهای کسب‌وکار، پروانه‌های صنفی، مجوزهای بهداشتی و صنعتی. خدمات تخصصی برای راه‌اندازی و توسعه کسب‌وکار شما.',
                'order': 5,
                'is_active': True
            },
            {
                'title': 'کارت بازرگانی',
                'icon': '💼',
                'short_description': 'اخذ و تمدید کارت بازرگانی، ثبت کدهای اقتصادی و انجام امور مربوط به واردات و صادرات.',
                'content': 'اخذ و تمدید کارت بازرگانی، ثبت کدهای اقتصادی و انجام امور مربوط به واردات و صادرات. خدمات جامع برای فعالیت‌های بازرگانی شما.',
                'order': 6,
                'is_active': True
            }
        ]
        
        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                title=service_data['title'],
                defaults=service_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created Service: {service.title}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Service already exists: {service.title}'))

        # Create Loan Categories and Items
        loan_categories_data = [
            {
                'title': 'وام مسکن',
                'icon': '🏠',
                'description': 'خرید و فروش وام مسکن با شرایط ویژه',
                'order': 1,
                'items': [
                    'وام خرید مسکن',
                    'وام ودیعه مسکن',
                    'وام بازسازی',
                    'وام تعمیرات'
                ]
            },
            {
                'title': 'وام خودرو',
                'icon': '🚗',
                'description': 'معامله وام خرید خودرو با نرخ رقابتی',
                'order': 2,
                'items': [
                    'وام خرید خودرو',
                    'وام نوسازی خودرو',
                    'تسهیلات خودرویی',
                    'لیزینگ خودرو'
                ]
            },
            {
                'title': 'وام کسب‌وکار',
                'icon': '💼',
                'description': 'تامین مالی برای کسب‌وکارها',
                'order': 3,
                'items': [
                    'وام سرمایه در گردش',
                    'وام خرید ماشین‌آلات',
                    'تسهیلات تولیدی',
                    'وام توسعه کسب‌وکار'
                ]
            }
        ]
        
        for category_data in loan_categories_data:
            category, created = LoanCategory.objects.get_or_create(
                title=category_data['title'],
                defaults={
                    'icon': category_data['icon'],
                    'description': category_data['description'],
                    'order': category_data['order']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created LoanCategory: {category.title}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'LoanCategory already exists: {category.title}'))
            
            # Create loan items for this category
            for item_title in category_data['items']:
                item, created = LoanItem.objects.get_or_create(
                    category=category,
                    title=item_title,
                    defaults={
                        'description': f'توضیحات مربوط به {item_title}',
                        'is_active': True
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created LoanItem: {item.title}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'LoanItem already exists: {item.title}'))

        # Create LeasingOffer
        leasing, created = LeasingOffer.objects.get_or_create(
            id=1,
            defaults={
                'title': 'لیزینگ خودرو با شرایط استثنایی',
                'description': 'خرید خودرو دیگر دغدغه شما نیست! با لیزینگ شهر راز، خودروی مورد نظر خود را با اقساط بلندمدت و بدون نیاز به وثیقه سنگین تهیه کنید.',
                'features': 'بدون پیش‌پرداخت\nاقساط بلندمدت\nبدون ضامن\nتحویل سریع',
                'stats': 'خودرو تحویل شده:500+\nرضایت مشتریان:98%\nماه اقساط:24\nپیش‌پرداخت:0%'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created LeasingOffer'))
        else:
            self.stdout.write(self.style.SUCCESS('LeasingOffer already exists'))

        # Create Registration Categories and Items
        registration_categories_data = [
            {
                'name': 'ثبت انواع شرکت',
                'icon': '🏢',
                'description': 'خدمات ثبت انواع شرکت‌ها',
                'items': [
                    {'title': 'ثبت شرکت سهامی خاص', 'cta_text': 'ثبت شرکت', 'cta_link': '#contact'},
                    {'title': 'ثبت شرکت با مسئولیت محدود', 'cta_text': 'ثبت شرکت', 'cta_link': '#contact'},
                    {'title': 'ثبت شرکت تعاونی', 'cta_text': 'ثبت شرکت', 'cta_link': '#contact'},
                    {'title': 'ثبت شرکت تضامنی', 'cta_text': 'ثبت شرکت', 'cta_link': '#contact'},
                    {'title': 'تغییرات شرکت', 'cta_text': 'ثبت شرکت', 'cta_link': '#contact'},
                    {'title': 'انحلال و ادغام شرکت', 'cta_text': 'ثبت شرکت', 'cta_link': '#contact'}
                ]
            },
            {
                'name': 'اخذ مجوزها',
                'icon': '📜',
                'description': 'خدمات اخذ انواع مجوزها',
                'items': [
                    {'title': 'مجوز کسب‌وکار', 'cta_text': 'اخذ مجوز', 'cta_link': '#contact'},
                    {'title': 'پروانه صنفی', 'cta_text': 'اخذ مجوز', 'cta_link': '#contact'},
                    {'title': 'مجوز بهداشتی', 'cta_text': 'اخذ مجوز', 'cta_link': '#contact'},
                    {'title': 'مجوز صنعتی', 'cta_text': 'اخذ مجوز', 'cta_link': '#contact'},
                    {'title': 'مجوز ساختمانی', 'cta_text': 'اخذ مجوز', 'cta_link': '#contact'},
                    {'title': 'مجوزهای تخصصی', 'cta_text': 'اخذ مجوز', 'cta_link': '#contact'}
                ]
            }
        ]
        
        for category_data in registration_categories_data:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={
                    'icon': category_data['icon'],
                    'description': category_data['description']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created Category: {category.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Category already exists: {category.name}'))
            
            # Create service items for this category
            for item_data in category_data['items']:
                item, created = ServiceItem.objects.get_or_create(
                    category=category,
                    title=item_data['title'],
                    defaults={
                        'description': f'توضیحات مربوط به {item_data["title"]}',
                        'cta_text': item_data['cta_text'],
                        'cta_link': item_data['cta_link']
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created ServiceItem: {item.title}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'ServiceItem already exists: {item.title}'))

        # Create WhyUsFeature (Features)
        features_data = [
            {'title': 'تجربه بیش از ۱۵ سال', 'icon': '⭐', 'description': 'تیم با تجربه و کارشناسی در حل مسائل حقوقی متنوع و پیچیده', 'order': 1},
            {'title': 'نرخ‌های رقابتی', 'icon': '💰', 'description': 'خدمات با کیفیت بالا و مناسب‌ترین قیمت برای تمام طبقات', 'order': 2},
            {'title': 'پاسخ سریع', 'icon': '⚡', 'description': 'پاسخگویی فوری به تمام درخواست‌ها و سؤال‌های کلاینت‌ها', 'order': 3},
            {'title': 'محرمانگی و امنیت', 'icon': '🔐', 'description': 'محفوظ بودن کامل اطلاعات و فایل‌های قضایی شما', 'order': 4},
            {'title': 'پشتیبانی ۲۴/۷', 'icon': '🕐', 'description': 'دسترسی دائمی به تیم حقوقی ما در تمام ساعات', 'order': 5},
            {'title': 'سیستم دیجیتال', 'icon': '💻', 'description': 'سیستمی پیشرفته برای مدیریت پرونده‌ها و مستندات', 'order': 6},
            {'title': 'تجزیه و تحلیل عمیق', 'icon': '📊', 'description': 'بررسی دقیق و تحلیل جامع هر پرونده قبل از شروع دفاع', 'order': 7},
            {'title': 'نتایج اثربخش', 'icon': '🎯', 'description': 'تمرکز بر دستیابی به بهترین نتایج برای هر پرونده', 'order': 8}
        ]
        
        for feature_data in features_data:
            feature, created = WhyUsFeature.objects.get_or_create(
                title=feature_data['title'],
                defaults=feature_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created WhyUsFeature: {feature.title}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'WhyUsFeature already exists: {feature.title}'))

        # Create Comparison
        comparison_data = [
            {'criterion': 'تجربه', 'our_value': '۱۵+ سال', 'others_value': 'متغیر'},
            {'criterion': 'تیم متخصص', 'our_value': '۵۰+ کارشناس', 'others_value': '۲-۵ نفر'},
            {'criterion': 'پاسخ سریع', 'our_value': '۲۴ ساعت', 'others_value': '۳-۷ روز'},
            {'criterion': 'سیستم دیجیتال', 'our_value': 'پیشرفته', 'others_value': 'محدود'},
            {'criterion': 'نرخ پذیرایی', 'our_value': 'شفاف و عادلانه', 'others_value': 'نامشخص'},
            {'criterion': 'نتایج موفق', 'our_value': '۹۵%', 'others_value': '۷۰%'},
            {'criterion': 'پشتیبانی ۲۴/۷', 'our_value': '✓ بلی', 'others_value': '✗ خیر'},
            {'criterion': 'مشاوره رایگان', 'our_value': '✓ بلی', 'others_value': '✗ خیر'}
        ]
        
        for comparison_item in comparison_data:
            item, created = Comparison.objects.get_or_create(
                criterion=comparison_item['criterion'],
                defaults=comparison_item
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created Comparison: {item.criterion}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Comparison already exists: {item.criterion}'))

        # Create Testimonials
        testimonials_data = [
            {
                'client_name': 'علی محمدی',
                'client_role': 'مدیرعامل شرکت',
                'comment': 'تیم شهر راز واقعاً حرفه‌ای و باتجربه است. پرونده‌ی ما را در کمترین وقت و بهترین نتیجه حل کردند. توصیه می‌کنم!',
                'rating': 5
            },
            {
                'client_name': 'فاطمه احمدی',
                'client_role': 'مالک کسب‌و‌کار',
                'comment': 'خدمات بسیار حرفه‌ای و کاملاً شفاف. هیچ هزینه پنهانی نداشت و نتیجه عالی بود. ممنونم!',
                'rating': 5
            },
            {
                'client_name': 'حسن رضایی',
                'client_role': 'بازرگان',
                'comment': 'سرعت پاسخگویی و مشاوره عالی. پیشنهادات قیمت رقابتی و نتایج بهتر از انتظار. بسیار رضایت‌مند!',
                'rating': 5
            }
        ]
        
        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                client_name=testimonial_data['client_name'],
                defaults=testimonial_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created Testimonial: {testimonial.client_name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Testimonial already exists: {testimonial.client_name}'))

        # Create FAQ
        faq_data = [
            {
                'question': 'چگونه می‌توانم وام خود را بفروشم؟',
                'answer': 'برای فروش وام، کافی است با ما تماس بگیرید و مشخصات وام خود را اعلام کنید. کارشناسان ما پس از بررسی، بهترین قیمت را به شما پیشنهاد می‌دهند و در صورت توافق، فرآیند انتقال وام آغاز می‌شود.',
                'order': 1,
                'is_active': True
            },
            {
                'question': 'مدت زمان ثبت شرکت چقدر است؟',
                'answer': 'مدت زمان ثبت شرکت بسته به نوع شرکت و کامل بودن مدارک، معمولاً بین 3 تا 7 روز کاری است. تیم ما تمام تلاش خود را می‌کند تا این فرآیند در کوتاه‌ترین زمان ممکن انجام شود.',
                'order': 2,
                'is_active': True
            },
            {
                'question': 'آیا لیزینگ خودرو نیاز به ضامن دارد؟',
                'answer': 'خیر، یکی از مزایای لیزینگ خودرو در شهر راز این است که نیازی به ضامن ندارد. شما می‌توانید با ارائه مدارک شناسایی و اثبات درآمد، از این خدمات استفاده کنید.',
                'order': 3,
                'is_active': True
            },
            {
                'question': 'هزینه خدمات حقوقی چگونه محاسبه می‌شود؟',
                'answer': 'هزینه خدمات حقوقی بسته به نوع پرونده، پیچیدگی موضوع و زمان مورد نیاز متفاوت است. ما پس از بررسی اولیه پرونده، هزینه‌ها را به صورت شفاف و دقیق به شما اعلام می‌کنیم.',
                'order': 4,
                'is_active': True
            },
            {
                'question': 'آیا مشاوره اولیه رایگان است؟',
                'answer': 'بله، مشاوره اولیه در تمام بخش‌های خدمات ما کاملاً رایگان است. شما می‌توانید با تماس با ما، از مشاوران متخصص ما راهنمایی‌های لازم را دریافت کنید.',
                'order': 5,
                'is_active': True
            },
            {
                'question': 'چگونه می‌توانم کارت بازرگانی دریافت کنم؟',
                'answer': 'برای دریافت کارت بازرگانی، ابتدا باید شرکت خود را ثبت کنید. سپس با ارائه مدارک مورد نیاز به اتاق بازرگانی، می‌توانید کارت بازرگانی دریافت کنید. تیم ما تمام این مراحل را برای شما انجام می‌دهد.',
                'order': 6,
                'is_active': True
            }
        ]
        
        for faq_item in faq_data:
            faq, created = FAQ.objects.get_or_create(
                question=faq_item['question'],
                defaults=faq_item
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created FAQ: {faq.question}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'FAQ already exists: {faq.question}'))

        # Create ContactInfo
        contact_info, created = ContactInfo.objects.get_or_create(
            id=1,
            defaults={
                'phone': '021-1234-5678\n0912-345-6789',
                'email': 'info@shahrar.ir\nsupport@shahrar.ir',
                'address': 'تهران، خیابان آزادی، پلاک ۱۲۳\nطبقه ۵، واحد ۱۰',
                'map_embed': ''
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created ContactInfo'))
        else:
            self.stdout.write(self.style.SUCCESS('ContactInfo already exists'))

        self.stdout.write(
            self.style.SUCCESS('Successfully initialized site with default Persian content')
        )