# News Analysis App

## How to Install (Developers)
1. Install python
2. Create and start virtual environment:
    1. python -m venv venv
    2. (macos/linux) source venv/bin/activate
    3. (windows) venv/Scripts/activate
3. pip install -r requirements.txt
4. Setup MySQL server
5. Connect app to MySQL server: in news_analysis_app/settings.py, add username and password for DATABASES

## How to start app

python manage.py runserver

## Resources:
https://docs.djangoproject.com/en/3.0/intro/tutorial01/
https://docs.djangoproject.com/en/3.0/howto/legacy-databases/