from django.conf.urls import include, url
from django.contrib import admin
from formupload import views
 
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^upload/', views.upload, name="upload"),
]