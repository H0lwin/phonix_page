#!/bin/bash
# Database Restore Script for Shahr-e Raze CMS

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
DB_NAME=${DB_NAME:-"shahreraze_db"}
DB_USER=${DB_USER:-"shahreraze_user"}

echo -e "${GREEN}Database Restore Script for Shahr-e Raze CMS${NC}"

# Check if backup file is provided
if [ $# -eq 0 ]; then
    echo -e "${RED}Usage: $0 <backup_file.sql or backup_file.sql.gz>${NC}"
    exit 1
fi

BACKUP_FILE=$1

# Check if backup file exists
if [ ! -f "$BACKUP_FILE" ]; then
    echo -e "${RED}Backup file not found: $BACKUP_FILE${NC}"
    exit 1
fi

echo -e "${YELLOW}Restoring database: $DB_NAME from $BACKUP_FILE${NC}"

# Confirm before proceeding
echo -e "${YELLOW}WARNING: This will overwrite the current database!${NC}"
read -p "Are you sure you want to continue? (y/N): " confirm

if [[ $confirm != [yY] ]]; then
    echo -e "${YELLOW}Restore cancelled.${NC}"
    exit 0
fi

# If the file is compressed, decompress it first
if [[ $BACKUP_FILE == *.gz ]]; then
    echo -e "${YELLOW}Decompressing backup file...${NC}"
    gunzip -c $BACKUP_FILE > /tmp/restore_backup.sql
    BACKUP_FILE="/tmp/restore_backup.sql"
fi

# Restore the database
echo -e "${YELLOW}Restoring database...${NC}"
mysql -u $DB_USER -p $DB_NAME < $BACKUP_FILE

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Database restore completed successfully!${NC}"
    
    # Clean up temporary file if we created one
    if [ -f "/tmp/restore_backup.sql" ]; then
        rm /tmp/restore_backup.sql
    fi
else
    echo -e "${RED}Database restore failed!${NC}"
    
    # Clean up temporary file if we created one
    if [ -f "/tmp/restore_backup.sql" ]; then
        rm /tmp/restore_backup.sql
    fi
    
    exit 1
fi