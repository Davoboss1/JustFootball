from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from transfers import views
app_name = "transfers"
urlpatterns = [
path('transfers/',views.transfers_league.as_view(),name="transfer"),



]
