#!/bin/bash
# Deployment script for Shahr-e Raze CMS

# Exit on any error
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting deployment process...${NC}"

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Install or update dependencies
echo -e "${YELLOW}Installing/updating dependencies...${NC}"
pip install -r requirements.txt

# Run migrations
echo -e "${YELLOW}Running database migrations...${NC}"
python manage.py migrate

# Collect static files
echo -e "${YELLOW}Collecting static files...${NC}"
python manage.py collectstatic --noinput -c

# Set proper permissions for static files
echo -e "${YELLOW}Setting permissions for static files...${NC}"
chmod -R 755 static/
chmod -R 644 static/**/*

# Set proper permissions for media files (if they exist)
if [ -d "media" ]; then
    echo -e "${YELLOW}Setting permissions for media files...${NC}"
    chmod -R 755 media/
fi

# Set proper permissions for the project directory
echo -e "${YELLOW}Setting permissions for project directory...${NC}"
chmod -R 755 .

echo -e "${GREEN}Deployment completed successfully!${NC}"
echo -e "${YELLOW}Remember to restart your web server and Django application.${NC}"