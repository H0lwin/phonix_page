@echo off
REM Script to update database credentials in the .env file

echo Updating database credentials in .env file...

REM Update the .env file with the correct database credentials
(
echo # Django Security Settings
echo SECRET_KEY=your-secret-key-here-change-this-in-production
echo DEBUG=False
echo.
echo # Host Settings
echo ALLOWED_HOSTS=localhost,127.0.0.1,citysecret.ir,www.citysecret.ir
echo.
echo # Database Settings
echo DB_NAME=shahreraze_cms_db
echo DB_USER=shahreraze_cms_user
echo DB_PASSWORD=your_actual_database_password_here
echo DB_HOST=localhost
echo DB_PORT=3306
echo.
echo # Path Settings
echo STATIC_ROOT=/var/www/phonix-page/static
echo MEDIA_ROOT=/var/www/phonix-page/media
echo.
echo # Additional Security Settings (uncomment in production)
echo SECURE_SSL_REDIRECT=True
echo SESSION_COOKIE_SECURE=True
echo CSRF_COOKIE_SECURE=True
) > C:\path\to\your\project\.env

echo Database credentials updated successfully!
echo Please replace 'your_actual_database_password_here' with the actual password.