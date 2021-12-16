from django.urls import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.news_home, name="news_home"),
    path('create', views.create, name="create"),
    path('news/<int:pk>', views.NewsDetailView, name="news-detail"),
]
