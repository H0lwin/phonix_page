#!/bin/bash
# Script to apply migrations in the correct order to avoid MySQL row size issues

echo "Applying migrations in the correct order to avoid MySQL row size issues..."

# Apply the initial migrations first
echo "Applying initial migrations..."
python manage.py migrate website 0002_sitesettings_comparison_subtitle_and_more

# Apply our custom migrations that fix the row size issue
echo "Applying custom migrations to fix row size issues..."
python manage.py migrate website 0011_fix_sitesettings_migration
python manage.py migrate website 0012_add_sitesettings_fields_properly
python manage.py migrate website 0013_handle_existing_fields

# Apply the split migrations
echo "Applying split migrations..."
python manage.py migrate website 0014_split_large_migration
python manage.py migrate website 0015_split_large_migration_part2
python manage.py migrate website 0016_split_large_migration_part3
python manage.py migrate website 0017_split_large_migration_part4
python manage.py migrate website 0018_split_large_migration_images

# Apply any remaining migrations
echo "Applying remaining migrations..."
python manage.py migrate

echo "All migrations applied successfully!"