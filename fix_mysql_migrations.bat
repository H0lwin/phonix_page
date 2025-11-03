@echo off
REM Script to fix MySQL migration issues

echo Fixing MySQL migration issues...

REM Backup the database first
echo Creating database backup...
mysqldump -u shahreraze_cms_user -p shahreraze_cms_db > backup_before_fix_%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%%time:~6,2%.sql

REM Check if backup was successful
if %errorlevel% equ 0 (
    echo Database backup created successfully
) else (
    echo Warning: Database backup failed, continuing anyway...
)

REM Remove migration records for the website app
echo Removing migration records from database...
mysql -u shahreraze_cms_user -p shahreraze_cms_db -e "DELETE FROM django_migrations WHERE app = 'website';"

REM Check if the command was successful
if %errorlevel% equ 0 (
    echo Migration records removed successfully
) else (
    echo Failed to remove migration records
    exit /b 1
)

REM Apply migrations in the correct order
echo Applying migrations...

REM Apply initial migrations
echo Applying initial migrations...
python manage.py migrate website 0002_sitesettings_comparison_subtitle_and_more

REM Apply our custom migrations
echo Applying custom migrations...
python manage.py migrate website 0011_fix_sitesettings_migration
python manage.py migrate website 0012_add_sitesettings_fields_properly
python manage.py migrate website 0013_handle_existing_fields

REM Apply split migrations
echo Applying split migrations...
python manage.py migrate website 0014_split_large_migration
python manage.py migrate website 0015_split_large_migration_part2
python manage.py migrate website 0016_split_large_migration_part3
python manage.py migrate website 0017_split_large_migration_part4
python manage.py migrate website 0018_split_large_migration_images

REM Apply remaining migrations
echo Applying remaining migrations...
python manage.py migrate

echo Migration fix completed!