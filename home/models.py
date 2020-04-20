from django.db import models
from news.models import football_posts
# Create your models here.
class slider(models.Model):
 	Title = models.CharField(max_length=45)
 	subtitle = models.CharField(max_length=100)
 	Post = models.ForeignKey(football_posts,on_delete=models.SET_NULL,null=True,blank=True)
 	image = models.ImageField(upload_to="news_images",null=True,blank=True)
 	
 	def __str__(self):
 		return str(self.Title)
