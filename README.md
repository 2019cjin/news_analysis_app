# News Analysis App

## Purpose
This app was created to visualize data on headlines gathered from multiple sources. This app should be used in conjunction with the News_Data_Analysis app, which gathers headlines data on a regular basis.

News_Data_Analysis app github: https://github.com/cjin2019/News_Data_Analysis

## How to Install Locally
1. Install python
2. Create and start virtual environment:
    1. python -m venv venv
    2. (macos/linux) source venv/bin/activate
    3. (windows) venv/Scripts/activate
3. pip install -r requirements.txt
4. Setup MySQL server: See instruction in readme here: 
5. Connect app to MySQL server: in news_analysis_app/settings.py, add username and password for DATABASES

## How to Run App Locally

python manage.py runserver

## Resources:

### Django
1. https://docs.djangoproject.com/en/3.0/intro/tutorial01/
2. https://docs.djangoproject.com/en/3.0/howto/legacy-databases/

### Javascript Files Used:
1. plotly: https://plotly.com/javascript
2. wordcloud resource: https://github.com/timdream/wordcloud2.js

### Frontend Styling Resources:
1. bootstrap: 
	1. https://getbootstrap.com/docs/3.4/components/#navbar
	2. https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html
2. icons: https://icons8.com/icons/set/bar-chart

### Resources for Deploying App:
1. Heroku: https://gist.github.com/randallreedjr/aa89e069371d07371882eea2df15fb4d
