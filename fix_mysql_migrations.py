#!/usr/bin/env python3
"""
Script to fix MySQL migration issues by resetting and reapplying migrations properly
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

def reset_migrations():
    """Reset migrations for the website app"""
    import MySQLdb
    from django.conf import settings
    
    # Get database settings
    db_settings = settings.DATABASES['default']
    
    try:
        # Connect to database
        conn = MySQLdb.connect(
            host=db_settings['HOST'],
            user=db_settings['USER'],
            passwd=db_settings['PASSWORD'],
            db=db_settings['NAME'],
            port=int(db_settings['PORT']) if db_settings['PORT'] else 3306
        )
        
        cursor = conn.cursor()
        
        # Check if django_migrations table exists
        cursor.execute("""
            SELECT COUNT(*) 
            FROM information_schema.tables 
            WHERE table_schema = %s AND table_name = 'django_migrations'
        """, (db_settings['NAME'],))
        
        result = cursor.fetchone()
        if result[0] == 0:
            print("django_migrations table does not exist")
            return False
            
        # Remove migration records for the website app
        cursor.execute("DELETE FROM django_migrations WHERE app = 'website'")
        print(f"Removed {cursor.rowcount} migration records for website app")
        
        # Check which website tables exist
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = %s AND table_name LIKE 'website_%'
        """, (db_settings['NAME'],))
        
        tables = [row[0] for row in cursor.fetchall()]
        print(f"Found website tables: {tables}")
        
        # Close connection
        conn.commit()
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"Error resetting migrations: {e}")
        return False

def apply_migrations():
    """Apply migrations in the correct order"""
    try:
        # Apply initial migrations
        print("Applying initial migrations...")
        execute_from_command_line(['manage.py', 'migrate', 'website', '0002'])
        
        # Apply our custom migrations
        print("Applying custom migrations...")
        execute_from_command_line(['manage.py', 'migrate', 'website', '0011'])
        execute_from_command_line(['manage.py', 'migrate', 'website', '0012'])
        execute_from_command_line(['manage.py', 'migrate', 'website', '0013'])
        
        # Apply split migrations
        print("Applying split migrations...")
        execute_from_command_line(['manage.py', 'migrate', 'website', '0014'])
        execute_from_command_line(['manage.py', 'migrate', 'website', '0015'])
        execute_from_command_line(['manage.py', 'migrate', 'website', '0016'])
        execute_from_command_line(['manage.py', 'migrate', 'website', '0017'])
        execute_from_command_line(['manage.py', 'migrate', 'website', '0018'])
        
        # Apply remaining migrations
        print("Applying remaining migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        return True
        
    except Exception as e:
        print(f"Error applying migrations: {e}")
        return False

if __name__ == "__main__":
    print("Fixing MySQL migration issues...")
    
    # Reset migrations
    if reset_migrations():
        print("Migration records reset successfully")
        
        # Apply migrations
        if apply_migrations():
            print("All migrations applied successfully!")
        else:
            print("Failed to apply migrations")
    else:
        print("Failed to reset migrations")