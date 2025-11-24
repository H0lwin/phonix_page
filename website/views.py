from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
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
    }
    
    return render(request, 'index.html', context)

def test_view(request):
    # Simple test view to verify data fetching
    site_settings = SiteSettings.objects.first()
    return HttpResponse(f"Test view - Site name: {site_settings.site_name if site_settings else 'No site settings found'}")

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