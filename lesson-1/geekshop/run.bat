@echo on

set project_dir=..\geekshop
set virtual_environment_dir=venv

cd "%project_dir%"

start "" "http://127.0.0.1:8000/"

call ..\%virtual_environment_dir%\Scripts\activate.bat
python manage.py runserver

pause