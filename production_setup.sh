#!/bin/bash
# Production setup script for Shahr-e Raze CMS

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting production setup for Shahr-e Raze CMS...${NC}"

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}Please run as root (sudo)${NC}"
  exit 1
fi

# Update system
echo -e "${YELLOW}Updating system packages...${NC}"
apt update && apt upgrade -y

# Install required packages
echo -e "${YELLOW}Installing required packages...${NC}"
apt install -y apache2 libapache2-mod-wsgi-py3 python3-dev python3-pip python3-venv

# Create project directory
echo -e "${YELLOW}Creating project directory...${NC}"
mkdir -p /var/www/phonix-page
chown -R www-data:www-data /var/www/phonix-page
chmod -R 755 /var/www/phonix-page

# Create virtual environment
echo -e "${YELLOW}Creating virtual environment...${NC}"
cd /var/www/phonix-page
sudo -u www-data python3 -m venv venv

# Activate virtual environment and install dependencies
echo -e "${YELLOW}Installing Python dependencies...${NC}"
sudo -u www-data bash -c "
  source venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
"

# Collect static files
echo -e "${YELLOW}Collecting static files...${NC}"
sudo -u www-data bash -c "
  source venv/bin/activate
  python manage.py collectstatic --noinput -c
"

# Set permissions for static files
echo -e "${YELLOW}Setting permissions for static files...${NC}"
chmod -R 755 static/
chown -R www-data:www-data static/

# Set permissions for media files (if they exist)
if [ -d "media" ]; then
  echo -e "${YELLOW}Setting permissions for media files...${NC}"
  chmod -R 755 media/
  chown -R www-data:www-data media/
fi

# Create environment variables file
echo -e "${YELLOW}Setting up environment variables...${NC}"
cat > /var/www/phonix-page/.env << EOF
SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(50))")
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,citysecret.ir,www.citysecret.ir
STATIC_ROOT=/var/www/phonix-page/static
MEDIA_ROOT=/var/www/phonix-page/media
EOF

# Copy Apache configuration
echo -e "${YELLOW}Configuring Apache...${NC}"
cp apache_config.conf /etc/apache2/sites-available/citysecret.ir.conf

# Enable site and required modules
echo -e "${YELLOW}Enabling site and modules...${NC}"
a2ensite citysecret.ir.conf
a2enmod ssl rewrite headers proxy proxy_http wsgi

# Test Apache configuration
echo -e "${YELLOW}Testing Apache configuration...${NC}"
apache2ctl configtest

echo -e "${GREEN}Production setup completed!${NC}"
echo -e "${YELLOW}Please remember to:${NC}"
echo -e "${YELLOW}1. Upload your project files to /var/www/phonix-page${NC}"
echo -e "${YELLOW}2. Update the database settings in settings.py${NC}"
echo -e "${YELLOW}3. Run migrations: python manage.py migrate${NC}"
echo -e "${YELLOW}4. Create a superuser: python manage.py createsuperuser${NC}"
echo -e "${YELLOW}5. Restart Apache: systemctl restart apache2${NC}"