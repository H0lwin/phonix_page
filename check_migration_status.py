#!/usr/bin/env python3
"""
Script to check the current migration status and database state
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

# Add the project directory to Python path
project_dir = '/var/www/phonix-page'
sys.path.append(project_dir)
sys.path.append(os.path.join(project_dir, 'cms_project'))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms_project.settings')

# Setup Django
django.setup()

def check_migration_status():
    """Check the current migration status"""
    try:
        # Show migration status
        print("=== Migration Status ===")
        execute_from_command_line(['manage.py', 'showmigrations', 'website'])
        
    except Exception as e:
        print(f"Error checking migration status: {e}")

def check_database_tables():
    """Check which tables exist in the database"""
    try:
        import MySQLdb
        from django.conf import settings
        
        # Get database settings
        db_settings = settings.DATABASES['default']
        
        # Connect to database
        conn = MySQLdb.connect(
            host=db_settings['HOST'],
            user=db_settings['USER'],
            passwd=db_settings['PASSWORD'],
            db=db_settings['NAME'],
            port=int(db_settings['PORT']) if db_settings['PORT'] else 3306
        )
        
        cursor = conn.cursor()
        
        # List all tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        print("\n=== Database Tables ===")
        for table in tables:
            print(table[0])
            
        # Check website tables specifically
        print("\n=== Website Tables ===")
        for table in tables:
            if table[0].startswith('website_'):
                print(table[0])
                
                # Show table structure
                cursor.execute(f"DESCRIBE {table[0]}")
                columns = cursor.fetchall()
                print(f"  Columns: {len(columns)}")
                if len(columns) < 20:  # Only show columns if not too many
                    for col in columns:
                        print(f"    {col[0]} ({col[1]})")
                else:
                    print("    (Too many columns to display)")
        
        # Close connection
        conn.close()
        
    except Exception as e:
        print(f"Error checking database tables: {e}")

if __name__ == "__main__":
    print("Checking migration and database status...")
    
    check_migration_status()
    check_database_tables()
    
    print("\nDone!")