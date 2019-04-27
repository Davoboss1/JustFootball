
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from . import views
from .models import football_posts

app_name = "news"

urlpatterns = [

path('news/',views.news,name = "news"),
path('news/<int:no>/<slug:title_url>',views.news, name = "news"),
path('news/<slug:title_url>',views.news , name = "news"),
path('news/post_news/',views.post_news.as_view(),name = "post_news"),
path('news/update_news/<pk>/<url>',views.update_news.as_view(),name="update_news"),
path('news/update_news/' ,views.update_news_url,name = "news_update"),
 path('news/delete_news/<pk>/<url>',views.delete_news.as_view(),name="delete_news"),
path('news/select_news_to_delete/' ,views.delete_news_url,name = "news_delete"),
 
 ]
