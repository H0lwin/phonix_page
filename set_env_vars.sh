#!/bin/bash
# Script to set environment variables for production deployment

# Set environment variables for Django
export SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(50))")
export DEBUG=False
export ALLOWED_HOSTS="localhost,127.0.0.1,citysecret.ir,www.citysecret.ir"
export STATIC_ROOT="/var/www/phonix-page/static"
export MEDIA_ROOT="/var/www/phonix-page/media"

echo "Environment variables set:"
echo "SECRET_KEY: $SECRET_KEY"
echo "DEBUG: $DEBUG"
echo "ALLOWED_HOSTS: $ALLOWED_HOSTS"
echo "STATIC_ROOT: $STATIC_ROOT"
echo "MEDIA_ROOT: $MEDIA_ROOT"