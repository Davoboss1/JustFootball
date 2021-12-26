from django.db import models
from django.forms import ModelForm , widgets
from django.utils.text import slugify
from scores.models import score
# Create your models here.
class football_posts(models.Model):
	
	Title = models.CharField(max_length = 100)
	match = models.OneToOneField(score,on_delete=models.SET_NULL,null=True,blank=True)
	image = models.ImageField(upload_to="news_images",null=True,blank=True)
	summary = models.CharField(max_length = 500,null=True , blank = True )
	news = models.TextField()
	url = models.SlugField(max_length=500,null=True,editable=False)
	created_at = models.DateTimeField(auto_now_add=True)
		
	def save(self,*args,**kwargs):
		self.url = slugify(self.Title,allow_unicode=True)
		super(football_posts,self).save(*args,**kwargs)
		
	def __str__(self):
		return self.Title
		
	def model_field_exists(cls, field):
		try:
			cls._meta.get_field(field)
			return True
		except models.FieldDoesNotExist:
			return False
	models.Model.field_exists = model_field_exists
	
	class Meta:
		ordering = ['-created_at']
	

class post_football(ModelForm):
	class Meta:
		model = football_posts
		fields = ('Title','match','image','summary','news')
		widgets = {
		'Title' : widgets.Textarea(attrs = {'cols' : 35 , 'rows' : 2 ,'placeholder' : 'Title',}),
		"match" : widgets.Select(attrs={"class" : "form-control","name":"news" ,"style":"max-width:350px",}),
		"match_news" : widgets.Select(attrs={"class" : "form-control","name":"news" ,"style":"max-width:350px",}),
		'images' : widgets.FileInput(attrs = {'placeholder' : 'Select image' , 'style' : 'width:100%',}),
		'summary' : widgets.Textarea(attrs = {'cols' : 35 , 'rows' : 3 , 'placeholder' : 'Summary' ,}),
		'news' : widgets.Textarea(attrs = {'cols' : 35 , 'rows' : 10 , 'id' : 'newstext' ,}),
		}
