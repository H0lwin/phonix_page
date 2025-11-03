#!/bin/bash
# Script to fix MySQL migration issues

echo "Fixing MySQL migration issues..."

# Backup the database first
echo "Creating database backup..."
mysqldump -u citysecret_admin -p citysecret > backup_before_fix_$(date +%Y%m%d_%H%M%S).sql

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "Database backup created successfully"
else
    echo "Warning: Database backup failed, continuing anyway..."
fi

# Remove migration records for the website app
echo "Removing migration records from database..."
mysql -u citysecret_admin -p citysecret -e "DELETE FROM django_migrations WHERE app = 'website';"

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "Migration records removed successfully"
else
    echo "Failed to remove migration records"
    exit 1
fi

# Apply migrations in the correct order
echo "Applying migrations..."

# Apply initial migrations
echo "Applying initial migrations..."
python manage.py migrate website 0002_sitesettings_comparison_subtitle_and_more

# Apply our custom migrations
echo "Applying custom migrations..."
python manage.py migrate website 0011_fix_sitesettings_migration
python manage.py migrate website 0012_add_sitesettings_fields_properly
python manage.py migrate website 0013_handle_existing_fields

# Apply split migrations
echo "Applying split migrations..."
python manage.py migrate website 0014_split_large_migration
python manage.py migrate website 0015_split_large_migration_part2
python manage.py migrate website 0016_split_large_migration_part3
python manage.py migrate website 0017_split_large_migration_part4
python manage.py migrate website 0018_split_large_migration_images

# Apply remaining migrations
echo "Applying remaining migrations..."
python manage.py migrate

echo "Migration fix completed!"