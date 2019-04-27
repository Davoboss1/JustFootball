from django.db import models

# Create your models here.
class Video(models.Model):
	video_name = models.CharField(max_length= 500,null=True,blank=True)
	embed_video_link = models.CharField(max_length= 1000)
	
	def __str__(self):
		return self.video_name + ' : ' + self.embed_video_link
