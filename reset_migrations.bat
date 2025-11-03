@echo off
REM Script to reset migrations for the website app

echo Resetting migrations for the website app...

REM Backup the current database
echo Creating database backup...
mysqldump -u shahreraze_cms_user -p shahreraze_cms_db > backup_before_reset_%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%%time:~6,2%.sql

REM Remove migration records for the website app
echo Removing migration records from database...
mysql -u shahreraze_cms_user -p shahreraze_cms_db -e "DELETE FROM django_migrations WHERE app = 'website';"

REM Optionally, you can also drop and recreate the tables
REM Uncomment the following lines if you want to start completely fresh
REM echo Dropping website tables...
REM mysql -u shahreraze_cms_user -p shahreraze_cms_db -e "DROP TABLE IF EXISTS website_sitesettings, website_herosection, website_statistic, website_service, website_loancategory, website_loanitem, website_leasingoffer, website_category, website_serviceitem, website_whyusfeature, website_comparison, website_testimonial, website_faq, website_contactinfo;"

echo Migration records removed. You can now run migrations again:
echo python manage.py migrate

echo Reset completed!