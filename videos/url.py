from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from . import views

app_name = "videos"

urlpatterns = [
path("videos/",views.Videos,name="Video")
]