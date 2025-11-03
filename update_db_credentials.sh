#!/bin/bash
# Script to update database credentials in the .env file

echo "Updating database credentials in .env file..."

# Update the .env file with the correct database credentials
cat > /var/www/phonix-page/.env << EOF
# Django Security Settings
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=False

# Host Settings
ALLOWED_HOSTS=localhost,127.0.0.1,citysecret.ir,www.citysecret.ir

# Database Settings
DB_NAME=shahreraze_cms_db
DB_USER=shahreraze_cms_user
DB_PASSWORD=your_actual_database_password_here
DB_HOST=localhost
DB_PORT=3306

# Path Settings
STATIC_ROOT=/var/www/phonix-page/static
MEDIA_ROOT=/var/www/phonix-page/media

# Additional Security Settings (uncomment in production)
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
EOF

echo "Database credentials updated successfully!"
echo "Please replace 'your_actual_database_password_here' with the actual password."