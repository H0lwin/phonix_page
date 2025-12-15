# 🔍 SEO Testing & Validation Checklist

## ✅ Pre-Launch SEO Testing

### 1. **Meta Tags Validation**

#### Title Tags
- [ ] Check each page has unique title (60-65 chars)
- [ ] Include primary keyword in title
- [ ] Brand name included
- [ ] Test: Open page in browser, check browser tab

**Command to Test:**
```bash
curl -s https://citysecret.ir/ | grep -o '<title[^>]*>[^<]*</title>'
```

#### Meta Description
- [ ] Each page has meta description (120-160 chars)
- [ ] Includes CTA (Call-To-Action)
- [ ] Does not exceed 160 characters
- [ ] Test: Use Chrome DevTools or SEO inspector

**Validation:**
```
Home: "{{ settings.site_name }} | خدمات مالی و حقوقی تخصصی"
Length: 51 chars ✓
```

#### Meta Keywords
- [ ] 5-10 keywords per page
- [ ] Include long-tail keywords
- [ ] Separate with commas
- [ ] Relevant to content

---

### 2. **Structured Data Validation**

#### Using Schema.org Validator
1. Go to: https://validator.schema.org/
2. Input: https://citysecret.ir/
3. Validate the following schemas are present:

**Required Schemas:**
- [ ] LocalBusiness ✓
- [ ] Organization ✓
- [ ] BreadcrumbList ✓
- [ ] WebPage ✓
- [ ] Service ✓
- [ ] FAQPage ✓
- [ ] AggregateRating ✓
- [ ] Review ✓

**Expected Output:** "JSON-LD validity: VALID"

#### Using Google Structured Data Test
1. Go to: https://search.google.com/test/rich-results
2. Input URL: https://citysecret.ir/
3. Check for:
   - [ ] No errors
   - [ ] Rich results eligible
   - [ ] Business details shown
   - [ ] Testimonials visible

---

### 3. **Mobile-Friendly Testing**

#### Using Google Mobile-Friendly Test
1. URL: https://search.google.com/test/mobile-friendly
2. Input: https://citysecret.ir/
3. Check:
- [ ] Page is mobile friendly ✓
- [ ] Viewport configured
- [ ] Touch elements properly spaced
- [ ] No horizontal scrolling
- [ ] Text is readable

#### Manual Mobile Testing
- [ ] Test on iPhone 12/13
- [ ] Test on Android (Samsung S22)
- [ ] Test with slow 3G connection
- [ ] Test with JavaScript disabled

---

### 4. **Sitemap & Robots.txt Validation**

#### Sitemap Testing
- [ ] File exists: https://citysecret.ir/sitemap.xml
- [ ] XML is valid
- [ ] All URLs listed
- [ ] Priorities set (0.0-1.0)
- [ ] Images included in sitemap
- [ ] Last modified dates present

**Test Command:**
```bash
curl -s https://citysecret.ir/sitemap.xml | head -20
```

**Expected Output:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
```

#### Robots.txt Testing
- [ ] File exists: https://citysecret.ir/robots.txt
- [ ] Contains Disallow rules
- [ ] Sitemap reference present
- [ ] Proper syntax
- [ ] Google-bot specific rules

**Test Command:**
```bash
curl -s https://citysecret.ir/robots.txt
```

**Expected Rules:**
```
User-agent: *
Allow: /
Disallow: /admin/
Sitemap: https://citysecret.ir/sitemap.xml
```

---

### 5. **Performance Testing**

#### Google PageSpeed Insights
1. URL: https://pagespeed.web.dev/
2. Input: https://citysecret.ir/
3. Validate:
- [ ] Performance score > 80
- [ ] Accessibility score > 90
- [ ] Best practices score > 90
- [ ] SEO score = 100
- [ ] Core Web Vitals - All "Good"

#### GTmetrix Analysis
1. URL: https://gtmetrix.com/
2. Input: https://citysecret.ir/
3. Check:
- [ ] Grade: A or B
- [ ] Page size < 3MB
- [ ] Load time < 3 seconds
- [ ] Requests < 100

#### WebPageTest
1. URL: https://www.webpagetest.org/
2. Test location: Iran (if available) or Europe
3. Review:
- [ ] First contentful paint < 2s
- [ ] Largest contentful paint < 2.5s
- [ ] Cumulative layout shift < 0.1

---

### 6. **Security Headers Testing**

#### Using SecurityHeaders.com
1. URL: https://securityheaders.com/
2. Input: https://citysecret.ir/
3. Verify headers:

**Expected Headers:**
```
✓ X-Content-Type-Options: nosniff
✓ X-Frame-Options: SAMEORIGIN
✓ X-XSS-Protection: 1; mode=block
✓ Strict-Transport-Security: max-age=31536000
✓ Referrer-Policy: strict-origin-when-cross-origin
✓ Permissions-Policy: (configured)
✓ Content-Security-Policy: (configured)
```

#### Manual Header Check
```bash
curl -i https://citysecret.ir/ | grep -E '^[A-Z]'
```

---

### 7. **Social Media Preview Testing**

#### Open Graph Tags
- [ ] Test on Facebook Sharing Debugger
  - URL: https://developers.facebook.com/tools/debug/
  - Input: https://citysecret.ir/
  - Check: Image, title, description display

- [ ] Test on LinkedIn
  - Copy URL to LinkedIn post
  - Verify preview image and text

- [ ] Test on Twitter/X
  - Use Twitter Card validator
  - URL: https://cards-dev.twitter.com/validator
  - Verify summary_large_image card

#### OG Tag Validation
```bash
curl -s https://citysecret.ir/ | grep "og:"
```

**Expected Output:**
```html
<meta property="og:type" content="website">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="...">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

---

### 8. **Search Engine Indexing**

#### Google Index Status
1. Go to: https://search.google.com/search-console
2. Check "Coverage" tab
3. Verify:
- [ ] All pages indexed
- [ ] No errors
- [ ] No excluded pages

#### Manual Indexing Check
```bash
# Check if page is indexed
site:citysecret.ir

# Check specific pages
site:citysecret.ir/#services
site:citysecret.ir/#contact
```

#### Bing Index Status
1. Go to: https://www.bing.com/webmasters
2. Submit sitemap
3. Monitor indexing status

---

### 9. **Link Analysis**

#### Internal Linking
- [ ] Home page links to all major sections
- [ ] Breadcrumbs implemented
- [ ] Navigation is logical
- [ ] No broken links

**Test Command:**
```bash
# Check for broken links
wget --spider -r https://citysecret.ir/ 2>&1 | grep -i 404
```

#### External Links
- [ ] Outbound links use proper rel attributes
- [ ] Links to authority sites
- [ ] Links have descriptive anchor text

---

### 10. **Accessibility Testing**

#### WAVE Web Accessibility Evaluation
1. URL: https://wave.webaim.org/
2. Input: https://citysecret.ir/
3. Check:
- [ ] No errors
- [ ] Few contrast errors
- [ ] Alt text on images
- [ ] Proper heading hierarchy

#### Using Lighthouse
```bash
# In Chrome DevTools
# Go to Lighthouse tab
# Select "Accessibility"
# Run audit
```

Target Score: > 90

---

### 11. **SEO Audit Using Tools**

#### Using SE Ranking
- [ ] Check keyword rankings
- [ ] Analyze competitor keywords
- [ ] Review backlink profile
- [ ] Monitor technical SEO

#### Using Semrush
- [ ] Technical SEO audit
- [ ] Site audit report
- [ ] Keyword research
- [ ] Backlink analysis

#### Using Ahrefs
- [ ] Site explorer
- [ ] Backlink checker
- [ ] Keyword research
- [ ] Content gap analysis

---

### 12. **Content Quality Assessment**

#### Readability
- [ ] Flesch Reading Ease > 60
- [ ] Clear hierarchy (H1, H2, H3)
- [ ] Short paragraphs (3-4 sentences)
- [ ] Active voice used
- [ ] No keyword stuffing

#### SEO Content Optimization
- [ ] Primary keyword in H1
- [ ] Keyword density 1-2%
- [ ] LSI keywords included
- [ ] Long-tail keywords targeted
- [ ] Word count > 300 (per section)

#### Using Yoast SEO Tool
(Install browser extension)
- [ ] Focus keyword set
- [ ] Readability analysis
- [ ] Keyword suggestions
- [ ] Content optimization tips

---

### 13. **Analytics Setup Validation**

#### Google Analytics 4
- [ ] Tracking ID configured
- [ ] Data collection working
- [ ] Goal tracking set up
- [ ] Conversion tracking active
- [ ] User properties defined

**Check Using:**
```javascript
// In browser console
gtag('event', 'page_view', {
  'page_path': window.location.pathname
});
```

#### Google Search Console
- [ ] Property verified
- [ ] Sitemap submitted
- [ ] Performance data showing
- [ ] No indexation issues
- [ ] Mobile usability > 90%

---

### 14. **Conversion Rate Optimization**

- [ ] CTA buttons are visible
- [ ] Contact form is working
- [ ] Phone numbers are clickable
- [ ] Testimonial form functional
- [ ] Lead capture setup

**Test CTAs:**
- [ ] "تماس با ما" button works
- [ ] "مشاوره رایگان" redirects correctly
- [ ] Forms submit successfully
- [ ] Thank you page appears

---

### 15. **Browser & Device Compatibility**

#### Desktop Browsers
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

#### Mobile Devices
- [ ] iPhone (Safari)
- [ ] Android (Chrome)
- [ ] iPad (Safari)
- [ ] Tablet (Android)

#### Screen Resolutions
- [ ] Mobile (320px - 640px)
- [ ] Tablet (641px - 1024px)
- [ ] Desktop (1025px - 1920px)
- [ ] Ultra-wide (1921px+)

---

## 🚀 Post-Launch Monitoring

### Weekly Tasks
- [ ] Check Google Search Console for errors
- [ ] Monitor keyword rankings
- [ ] Review site analytics
- [ ] Check for broken links
- [ ] Monitor page load speed

### Monthly Tasks
- [ ] Full SEO audit using tool
- [ ] Competitor analysis
- [ ] Content performance review
- [ ] Backlink analysis
- [ ] Traffic trend analysis

### Quarterly Tasks
- [ ] Comprehensive technical SEO audit
- [ ] Content strategy review
- [ ] Link building campaign assessment
- [ ] Mobile usability test
- [ ] Security audit

---

## 📊 Success Metrics

### Target Goals (3 months)
- [ ] 100+ pages indexed
- [ ] 50+ organic sessions/month
- [ ] 10+ keyword rankings in top 100
- [ ] 2+ keyword rankings in top 10
- [ ] Zero indexing errors

### Target Goals (6 months)
- [ ] 1000+ organic sessions/month
- [ ] 100+ keyword rankings in top 100
- [ ] 20+ keyword rankings in top 10
- [ ] 1+ keyword ranking #1
- [ ] 5000+ backlinks

### Target Goals (12 months)
- [ ] 5000+ organic sessions/month
- [ ] 500+ keyword rankings in top 100
- [ ] 100+ keyword rankings in top 10
- [ ] 10+ keyword rankings #1
- [ ] Domain authority > 30

---

## 🛠️ Tools Checklist

**Essential Tools:**
- [ ] Google Search Console
- [ ] Google Analytics 4
- [ ] Google PageSpeed Insights
- [ ] Schema.org Validator
- [ ] Mobile-Friendly Test

**Recommended Tools:**
- [ ] Semrush/Ahrefs/SE Ranking
- [ ] Screaming Frog
- [ ] Ubersuggest
- [ ] Moz Pro
- [ ] Surfer SEO

**Useful Browser Extensions:**
- [ ] SEO Analyzer
- [ ] Wappalyzer
- [ ] META SEO Inspector
- [ ] Lighthouse
- [ ] WAVE (Accessibility)

---

**Created:** 2025-12-14  
**Status:** Ready for Implementation  
**Next Review:** After 1 Month of Launch
