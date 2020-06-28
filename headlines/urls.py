from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /headlines/news_websites/
    path('news_websites/', views.news_websites, name='news_websites'),
]
