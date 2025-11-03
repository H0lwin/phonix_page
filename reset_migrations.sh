#!/bin/bash
# Script to reset migrations for the website app

echo "Resetting migrations for the website app..."

# Backup the current database
echo "Creating database backup..."
mysqldump -u citysecret_admin -p citysecret > backup_before_reset_$(date +%Y%m%d_%H%M%S).sql

# Remove migration records for the website app
echo "Removing migration records from database..."
mysql -u citysecret_admin -p citysecret -e "DELETE FROM django_migrations WHERE app = 'website';"

# Optionally, you can also drop and recreate the tables
# Uncomment the following lines if you want to start completely fresh
# echo "Dropping website tables..."
# mysql -u citysecret_admin -p citysecret -e "DROP TABLE IF EXISTS website_sitesettings, website_herosection, website_statistic, website_service, website_loancategory, website_loanitem, website_leasingoffer, website_category, website_serviceitem, website_whyusfeature, website_comparison, website_testimonial, website_faq, website_contactinfo;"

echo "Migration records removed. You can now run migrations again:"
echo "python manage.py migrate"

echo "Reset completed!"
