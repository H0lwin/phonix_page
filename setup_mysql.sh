#!/bin/bash
# MySQL Database Setup Script for Shahr-e Raze CMS

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}MySQL Database Setup for Shahr-e Raze CMS${NC}"

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}Please run as root (sudo)${NC}"
  exit 1
fi

# Install MySQL server and client if not already installed
echo -e "${YELLOW}Installing MySQL server and client...${NC}"
apt update
apt install -y mysql-server mysql-client libmysqlclient-dev

# Start MySQL service
echo -e "${YELLOW}Starting MySQL service...${NC}"
systemctl start mysql
systemctl enable mysql

# Secure MySQL installation
echo -e "${YELLOW}Securing MySQL installation...${NC}"
mysql_secure_installation

# Create database and user
echo -e "${YELLOW}Creating database and user...${NC}"
read -p "Enter MySQL root password: " root_password
read -p "Enter database name (default: shahreraze_db): " db_name
read -p "Enter database user (default: shahreraze_user): " db_user

# Set defaults if not provided
db_name=${db_name:-shahreraze_db}
db_user=${db_user:-shahreraze_user}

# Generate random password for database user
db_password=$(openssl rand -base64 32 | tr -d "=+/" | cut -c1-25)

# Create database and user
mysql -u root -p"$root_password" <<EOF
CREATE DATABASE IF NOT EXISTS $db_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS '$db_user'@'localhost' IDENTIFIED BY '$db_password';
GRANT ALL PRIVILEGES ON $db_name.* TO '$db_user'@'localhost';
FLUSH PRIVILEGES;
EOF

echo -e "${GREEN}Database setup completed!${NC}"
echo -e "${YELLOW}Database name: $db_name${NC}"
echo -e "${YELLOW}Database user: $db_user${NC}"
echo -e "${YELLOW}Database password: $db_password${NC}"
echo -e "${YELLOW}Please add these credentials to your environment variables or .env file:${NC}"
echo -e "${YELLOW}DB_NAME=$db_name${NC}"
echo -e "${YELLOW}DB_USER=$db_user${NC}"
echo -e "${YELLOW}DB_PASSWORD=$db_password${NC}"
echo -e "${YELLOW}DB_HOST=localhost${NC}"
echo -e "${YELLOW}DB_PORT=3306${NC}"