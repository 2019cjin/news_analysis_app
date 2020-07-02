from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'headlines'
urlpatterns = [
    path('', views.index, name='index'),
    path('sentiment', views.chart_neg_pos, name = 'sentiment'),
    path('keyword_cloud', views.keyword_cloud, name = 'keyword_cloud'),
    path('keyword/<str:word>/', views.headline_display, name = 'keyword')
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)