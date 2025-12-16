from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
import gzip
import re

class SEOOptimizationMiddleware(MiddlewareMixin):
    
    def process_response(self, request, response):
        if request.path in ['/robots.txt', '/sitemap.xml', '/admin/']:
            return response
        
        if response.status_code == 200 and 'text/html' in response.get('Content-Type', ''):
            try:
                response = self._add_security_headers(response)
                response = self._add_performance_headers(response)
                response = self._add_cache_headers(response, request)
                response = self._optimize_html(response)
            except Exception as e:
                pass
        
        return response
    
    def _add_security_headers(self, response):
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'SAMEORIGIN'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://fonts.googleapis.com https://cdn.jsdelivr.net https://static.cloudflareinsights.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; media-src 'self' https:; connect-src 'self' https:;"
        return response
    
    def _add_performance_headers(self, response):
        response['X-DNS-Prefetch-Control'] = 'on'
        response['X-Content-Type-Options'] = 'nosniff'
        
        response['Link'] = '; '.join([
            '<https://fonts.googleapis.com>; rel=preconnect; crossorigin',
            '<https://fonts.gstatic.com>; rel=preconnect; crossorigin',
            '<https://cdn.jsdelivr.net>; rel=preconnect',
        ])
        
        return response
    
    def _add_cache_headers(self, response, request):
        if request.path == '/':
            response['Cache-Control'] = 'public, max-age=3600'
        elif request.path in ['/robots.txt', '/sitemap.xml']:
            response['Cache-Control'] = 'public, max-age=86400'
        else:
            response['Cache-Control'] = 'public, max-age=300'
        
        return response
    
    def _optimize_html(self, response):
        try:
            content = response.content.decode('utf-8')
            
            content = self._add_preload_hints(content)
            content = self._optimize_images(content)
            content = self._minify_whitespace(content)
            
            response.content = content.encode('utf-8')
            response['Content-Length'] = len(response.content)
        except Exception as e:
            pass
        
        return response
    
    def _add_preload_hints(self, content):
        preload_hints = (
            '<link rel="preload" as="font" href="https://fonts.gstatic.com/s/vazirmatn/..." crossorigin>\n'
            '<link rel="prefetch" href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap">\n'
        )
        
        if '<head>' in content:
            content = content.replace(
                '<link rel="preconnect" href="https://fonts.googleapis.com">',
                '<link rel="preconnect" href="https://fonts.googleapis.com">\n' + preload_hints
            )
        
        return content
    
    def _optimize_images(self, content):
        content = re.sub(
            r'<img([^>]*)>',
            lambda m: self._add_img_attributes(m.group(1)),
            content,
            flags=re.IGNORECASE
        )
        return content
    
    def _add_img_attributes(self, attrs):
        if 'loading=' not in attrs.lower():
            attrs += ' loading="lazy"'
        
        if 'decoding=' not in attrs.lower():
            attrs += ' decoding="async"'
        
        return f'<img{attrs}>'
    
    def _minify_whitespace(self, content):
        content = re.sub(r'\n\s+\n', '\n', content)
        content = re.sub(r'  +', ' ', content)
        return content


class RobotsMetaHeaderMiddleware(MiddlewareMixin):
    
    def process_response(self, request, response):
        
        if response.status_code == 200 and 'text/html' in response.get('Content-Type', ''):
            if '/admin/' not in request.path:
                response['X-Robots-Tag'] = 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'
        elif response.status_code == 404:
            response['X-Robots-Tag'] = 'noindex, nofollow'
        elif response.status_code == 500:
            response['X-Robots-Tag'] = 'noindex, nofollow'
        
        return response


class CompressResponseMiddleware(MiddlewareMixin):
    
    def process_response(self, request, response):
        if response.status_code != 200:
            return response
        
        if 'gzip' in request.META.get('HTTP_ACCEPT_ENCODING', ''):
            if response.has_header('Content-Type'):
                content_type = response['Content-Type']
                if any(ct in content_type for ct in ['text/html', 'application/json', 'text/plain', 'text/css']):
                    content = response.content
                    if len(content) > 1000:
                        gzipped_content = gzip.compress(content)
                        if len(gzipped_content) < len(content):
                            response.content = gzipped_content
                            response['Content-Encoding'] = 'gzip'
                            response['Content-Length'] = len(gzipped_content)
        
        return response
