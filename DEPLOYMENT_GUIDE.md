# راهنمای استقرار Phonix Page بر روی سرور Ubuntu با Apache

## مرحله ۱: آماده‌سازی سرور

### ۱.۱ بروزرسانی سیستم
```bash
sudo apt update && sudo apt upgrade -y
```

### ۱.۲ نصب بسته‌های مورد نیاز
```bash
sudo apt install -y python3 python3-pip python3-venv git apache2 apache2-dev libapache2-mod-wsgi-py3 postgresql postgresql-contrib
```

## مرحله ۲: کلونش مخزن

### ۲.۱ ایجاد دایرکتوری پروژه
```bash
sudo mkdir -p /var/www/phonix_page
sudo chown $USER:$USER /var/www/phonix_page
cd /var/www/phonix_page
```

### ۲.۲ کلون کردن مخزن
```bash
git clone https://github.com/H0lwin/phonix_page.git .
```

## مرحله ۳: تنظیم محیط Python

### ۳.۱ ایجاد Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### ۳.۲ نصب dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## مرحله ۴: تنظیم متغیرهای محیط

### ۴.۱ کپی کردن فایل .env
```bash
cp .env.example .env
```

### ۴.۲ ویرایش فایل .env
```bash
nano .env
```

**تنظیمات ضروری:**
```
DEBUG=False
ALLOWED_HOSTS=your_domain.com,www.your_domain.com,your_server_ip
SECRET_KEY=[خروجی دستور زیر]
```

### ۴.۳ تولید SECRET_KEY
```bash
python3 generate_secret_key.py
```

## مرحله ۵: تنظیم Django

### ۵.۱ مایگریشن دیتابیس
```bash
python3 manage.py migrate
```

### ۵.۲ جمع‌آوری Static Files
```bash
python3 manage.py collectstatic --noinput
```

### ۵.۳ ایجاد Super User (Optional)
```bash
python3 manage.py createsuperuser
```

## مرحله ۶: تنظیم Apache

### ۶.۱ فعال کردن ماژول WSGI
```bash
sudo a2enmod wsgi
```

### ۶.۲ ایجاد فایل VirtualHost Apache
```bash
sudo nano /etc/apache2/sites-available/phonix_page.conf
```

**محتوای فایل:**
```apache
<VirtualHost *:80>
    ServerName your_domain.com
    ServerAlias www.your_domain.com
    ServerAdmin admin@your_domain.com

    ErrorLog ${APACHE_LOG_DIR}/phonix_error.log
    CustomLog ${APACHE_LOG_DIR}/phonix_access.log combined

    Alias /static /var/www/phonix_page/staticfiles/
    <Directory /var/www/phonix_page/staticfiles>
        Require all granted
    </Directory>

    Alias /media /var/www/phonix_page/media/
    <Directory /var/www/phonix_page/media>
        Require all granted
    </Directory>

    <Directory /var/www/phonix_page/cms_project>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess phonix_page python-home=/var/www/phonix_page/venv python-path=/var/www/phonix_page
    WSGIProcessGroup phonix_page
    WSGIScriptAlias / /var/www/phonix_page/cms_project/wsgi.py

</VirtualHost>
```

### ۶.۳ فعال کردن سایت
```bash
sudo a2ensite phonix_page.conf
sudo a2dissite 000-default.conf
```

### ۶.۴ تست تنظیمات Apache
```bash
sudo apache2ctl configtest
```
**انتظار برای خروجی:** `Syntax OK`

## مرحله ۷: تنظیم مجوزها

```bash
sudo chown -R www-data:www-data /var/www/phonix_page
sudo chmod -R 755 /var/www/phonix_page
sudo chmod -R 775 /var/www/phonix_page/media
```

## مرحله ۸: راه‌اندازی Apache

### ۸.۱ شروع سرویس Apache
```bash
sudo systemctl restart apache2
```

### ۸.۲ فعال‌سازی Apache هنگام شروع سیستم
```bash
sudo systemctl enable apache2
```

### ۸.۳ بررسی وضعیت Apache
```bash
sudo systemctl status apache2
```

## مرحله ۹: تنظیم SSL (بیاد داشت: بسیار توصیه‌شده است)

### ۹.۱ نصب Certbot
```bash
sudo apt install -y certbot python3-certbot-apache
```

### ۹.۲ صدور گواهی SSL
```bash
sudo certbot --apache -d your_domain.com -d www.your_domain.com
```

## مرحله ۱۰: تست و بررسی نهایی

### ۱۰.۱ بررسی لاگ‌ها
```bash
sudo tail -f /var/log/apache2/phonix_error.log
sudo tail -f /var/log/apache2/phonix_access.log
```

### ۱۰.۲ دسترسی وب
- در مرورگر به آدرس دامنه خود مراجعه کنید
- بررسی کنید که سایت به درستی بارگذاری شود
- بررسی صفحه Admin در `/admin`

## مرحله ۱۱: نگهداری و بهینه‌سازی

### ۱۱.۱ راه‌اندازی مجدد
اگر تغییراتی انجام دادید:
```bash
cd /var/www/phonix_page
source venv/bin/activate
git pull origin master
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput
sudo systemctl restart apache2
```

### ۱۱.۲ مانیتورینگ
```bash
sudo systemctl status apache2
ps aux | grep wsgi
```

## نکات مهم

- ✅ `ALLOWED_HOSTS` را با دامنه صحیح تنظیم کنید
- ✅ `DEBUG=False` برای محیط Production
- ✅ مجوزها را برای کاربر `www-data` تنظیم کنید
- ✅ SSL/TLS استفاده کنید (Certbot)
- ✅ پایگاه‌داده را محافظت کنید
- ✅ لاگ‌ها را مراقبت کنید
- ✅ Backup منظم تهیه کنید

## حل مشکلات

### خطای Permission Denied
```bash
sudo chown -R www-data:www-data /var/www/phonix_page
sudo chmod -R u+w /var/www/phonix_page/media
```

### خطای Module Not Found
```bash
source /var/www/phonix_page/venv/bin/activate
pip install -r requirements.txt
```

### Apache نتوانست شروع شود
```bash
sudo apache2ctl configtest
sudo tail -f /var/log/apache2/error.log
```

