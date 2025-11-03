@echo off
REM Deployment script for Shahr-e Raze CMS on Windows

echo Starting deployment process...

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install or update dependencies
echo Installing/updating dependencies...
pip install -r requirements.txt

REM Run migrations
echo Running database migrations...
python manage.py migrate

REM Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput -c

REM Set proper permissions for static files (Windows version)
echo Setting permissions for static files...
icacls staticfiles /grant Users:(OI)(CI)R /T

REM Set proper permissions for media files (if they exist)
if exist media (
    echo Setting permissions for media files...
    icacls media /grant Users:(OI)(CI)R /T
)

echo Deployment completed successfully!
echo Remember to restart your web server and Django application.