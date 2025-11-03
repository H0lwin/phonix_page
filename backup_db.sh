#!/bin/bash
# Database Backup Script for Shahr-e Raze CMS

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
DB_NAME=${DB_NAME:-"shahreraze_db"}
DB_USER=${DB_USER:-"shahreraze_user"}
BACKUP_DIR="/var/backups/shahreraze"
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_$DATE.sql"

echo -e "${GREEN}Starting database backup...${NC}"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Create database backup
echo -e "${YELLOW}Creating backup of database: $DB_NAME${NC}"
mysqldump -u $DB_USER -p $DB_NAME > $BACKUP_FILE

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Database backup completed successfully!${NC}"
    echo -e "${YELLOW}Backup file: $BACKUP_FILE${NC}"
    
    # Compress the backup
    echo -e "${YELLOW}Compressing backup file...${NC}"
    gzip $BACKUP_FILE
    echo -e "${GREEN}Backup compressed successfully!${NC}"
    echo -e "${YELLOW}Compressed backup file: $BACKUP_FILE.gz${NC}"
    
    # Remove backups older than 30 days
    echo -e "${YELLOW}Removing old backups (older than 30 days)...${NC}"
    find $BACKUP_DIR -name "${DB_NAME}_*.sql.gz" -mtime +30 -delete
    echo -e "${GREEN}Old backups removed successfully!${NC}"
else
    echo -e "${RED}Database backup failed!${NC}"
    exit 1
fi