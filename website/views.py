from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import condition
import json
from .models import (
    SiteSettings,
    HeroSection,
    Statistic,
    Service,
    LoanCategory,
    LeasingOffer,
    Category,
    ServiceItem,
    WhyUsFeature,
    Comparison,
    Testimonial,
    FAQ,
    ContactInfo,
    CollaborationProcess,
    Company,
)

def index(request):
    # Fetch all required data for the template
    context = {
        'settings': SiteSettings.objects.first(),
        'hero': HeroSection.objects.first(),
        'stats': Statistic.objects.all(),
        'services': Service.objects.filter(is_active=True),
        'loan_categories': LoanCategory.objects.prefetch_related('loanitem_set'),
        'registration_categories': Category.objects.prefetch_related('serviceitem_set'),
        'leasing': LeasingOffer.objects.first(),
        'features': WhyUsFeature.objects.all(),
        'comparison': Comparison.objects.all(),
        'testimonials': Testimonial.objects.filter(status='approved'),
        'faq': FAQ.objects.filter(is_active=True),
        'contact': ContactInfo.objects.first(),
        'collaboration_process': CollaborationProcess.objects.prefetch_related('steps').first(),
        'companies': Company.objects.filter(is_active=True),
    }
    
    return render(request, 'index.html', context)

def test_view(request):
    # Simple test view to verify data fetching
    site_settings = SiteSettings.objects.first()
    return HttpResponse(f"Test view - Site name: {site_settings.site_name if site_settings else 'No site settings found'}")

def robots_txt(request):
    robots_content = """# Robots.txt for SEO optimization

# Allow all bots
User-agent: *
Allow: /
Allow: /static/
Allow: /media/

# Disallow unnecessary paths
Disallow: /admin/
Disallow: /static/admin/
Disallow: /api/
Disallow: /*.json$
Disallow: /*?*=*
Disallow: /*?*sort=*

# Crawl delay
Crawl-delay: 1

# Request rate
Request-rate: 30/60

# Sitemap location - CRITICAL for SEO
Sitemap: https://citysecret.ir/sitemap.xml

# Specific rules for Google Bot (favorable)
User-agent: Googlebot
Allow: /
Crawl-delay: 0

# Specific rules for Bing
User-agent: Bingbot
Allow: /
Crawl-delay: 1
"""
    return HttpResponse(robots_content, content_type='text/plain')

def sitemap_xml(request):
    settings_obj = SiteSettings.objects.first()
    
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
        xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">

  <!-- Home Page with Images -->
  <url>
    <loc>https://citysecret.ir/</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
'''
    
    if settings_obj and settings_obj.logo:
        sitemap_content += f'''    <image:image>
      <image:loc>https://citysecret.ir{settings_obj.logo.url}</image:loc>
      <image:title>{settings_obj.site_name}</image:title>
    </image:image>
'''
    
    sitemap_content += '''  </url>

  <!-- Services Section -->
  <url>
    <loc>https://citysecret.ir/#services</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Loan Services Section -->
  <url>
    <loc>https://citysecret.ir/#loan-services</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Leasing Section -->
  <url>
    <loc>https://citysecret.ir/#leasing</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
'''
    
    leasing = LeasingOffer.objects.first()
    if leasing and leasing.image:
        sitemap_content += f'''    <image:image>
      <image:loc>https://citysecret.ir{leasing.image.url}</image:loc>
      <image:title>{leasing.title}</image:title>
    </image:image>
'''
    
    sitemap_content += '''  </url>

  <!-- Registration & Licenses Section -->
  <url>
    <loc>https://citysecret.ir/#registration</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>

  <!-- Process Section -->
  <url>
    <loc>https://citysecret.ir/#process</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>

  <!-- Features Section -->
  <url>
    <loc>https://citysecret.ir/#features</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>

  <!-- Comparison Section -->
  <url>
    <loc>https://citysecret.ir/#comparison</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>

  <!-- Testimonials Section -->
  <url>
    <loc>https://citysecret.ir/#testimonials</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>

  <!-- Trust Section -->
  <url>
    <loc>https://citysecret.ir/#trust</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>

  <!-- FAQ Section -->
  <url>
    <loc>https://citysecret.ir/#faq</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>

  <!-- Partner Companies Section -->
  <url>
    <loc>https://citysecret.ir/#companies</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
'''
    
    companies = Company.objects.filter(is_active=True)
    for company in companies:
        if company.logo:
            sitemap_content += f'''    <image:image>
      <image:loc>https://citysecret.ir{company.logo.url}</image:loc>
      <image:title>{company.name}</image:title>
    </image:image>
'''
    
    sitemap_content += '''  </url>

  <!-- Contact Section -->
  <url>
    <loc>https://citysecret.ir/#contact</loc>
    <lastmod>2025-12-14</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>

</urlset>'''
    
    return HttpResponse(sitemap_content, content_type='application/xml')

@method_decorator(csrf_exempt, name='dispatch')
class SubmitTestimonialView(View):
    def post(self, request):
        try:
            # Get data from request
            data = json.loads(request.body)
            client_name = data.get('client_name')
            client_role = data.get('client_role')
            rating = int(data.get('rating'))
            comment = data.get('comment')
            
            # Validate required fields
            if not client_name or not client_role or not comment:
                return JsonResponse({
                    'success': False,
                    'message': 'لطفاً تمام فیلدهای اجباری را پر کنید.'
                })
            
            # Create new testimonial with pending status
            testimonial = Testimonial.objects.create(
                client_name=client_name,
                client_role=client_role,
                rating=rating,
                comment=comment,
                status='pending'
            )
            
            return JsonResponse({
                'success': True,
                'message': 'نظر شما با موفقیت ثبت شد و پس از تایید توسط مدیریت در سایت نمایش داده خواهد شد.'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'خطا در ثبت نظر. لطفاً دوباره تلاش کنید.'
            })