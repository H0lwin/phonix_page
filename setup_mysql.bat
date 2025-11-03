@echo off
REM MySQL Database Setup Script for Shahr-e Raze CMS on Windows

echo MySQL Database Setup for Shahr-e Raze CMS

REM Check if MySQL is installed
mysql --version >nul 2>&1
if %errorlevel% neq 0 (
    echo MySQL is not installed or not in PATH
    echo Please install MySQL Server first
    pause
    exit /b 1
)

REM Start MySQL service
echo Starting MySQL service...
net start MySQL80 >nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to start MySQL service
    echo Please ensure MySQL is properly installed
    pause
    exit /b 1
)

REM Create database and user
echo Creating database and user...
set /p root_password="Enter MySQL root password: "

REM Set defaults
set db_name=shahreraze_db
set db_user=shahreraze_user

REM Generate random password for database user
powershell -Command "$password = -join ((65..90) + (97..122) | Get-Random -Count 25 | % {[char]$_}); Write-Host $password" > temp_password.txt
set /p db_password=<temp_password.txt
del temp_password.txt

REM Create database and user
mysql -u root -p%root_password% -e "CREATE DATABASE IF NOT EXISTS %db_name% CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u root -p%root_password% -e "CREATE USER IF NOT EXISTS '%db_user%'@'localhost' IDENTIFIED BY '%db_password%';"
mysql -u root -p%root_password% -e "GRANT ALL PRIVILEGES ON %db_name%.* TO '%db_user%'@'localhost';"
mysql -u root -p%root_password% -e "FLUSH PRIVILEGES;"

echo Database setup completed!
echo Database name: %db_name%
echo Database user: %db_user%
echo Database password: %db_password%
echo Please add these credentials to your environment variables:
echo DB_NAME=%db_name%
echo DB_USER=%db_user%
echo DB_PASSWORD=%db_password%
echo DB_HOST=localhost
echo DB_PORT=3306

pause