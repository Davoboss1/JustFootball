from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.urls import include
from django.conf.urls import url
from . import views
from .models import *


app_name = "standings"




urlpatterns = [

path('standings/<league_url>/',views.standings,name="standing"),
path('standings/', views.standings,name = "standing"),
]
