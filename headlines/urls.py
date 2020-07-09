from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'headlines'
urlpatterns = [
    path('', views.index, name='index'),
    path('sentiment', views.chart_neg_pos, name = 'sentiment'),
    path('keyword_cloud', views.keyword_cloud, name = 'keyword_cloud'),
    path('headline_filter/<str:word>/', views.headline_display, name = 'headline_filter'),
    path('keyword_list', views.keyword_display, name = "keyword_list"),
    path('news_websites/', views.news_websites, name='news_websites'),
    path('about/', views.about, name='about'),
    path('process/', views.process, name='process')
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

