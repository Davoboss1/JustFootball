from django.db import models
from django.forms import ModelForm , widgets
from django.utils.text import slugify
from scores.models import score
# Create your models here.
class football_posts(models.Model):
	
	Title = models.CharField(max_length = 100)
	match = models.OneToOneField(score,on_delete=models.SET_NULL,null=True,blank=True)
	images = models.URLField()
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
		fields = ('Title','match','images','summary','news')
		widgets = {
		'Title' : widgets.Textarea(attrs = {'cols' : 35 , 'rows' : 2 ,'placeholder' : 'Title',}),
		
		"match_news" : widgets.Select(attrs={"name":"news" ,"style":"width:50%",}),
		'images' : widgets.URLInput(attrs = {'placeholder' : 'Images Links' , 'style' : 'width:100%',}),
		'summary' : widgets.Textarea(attrs = {'cols' : 35 , 'rows' : 3 , 'placeholder' : 'Summary' ,}),
		'news' : widgets.Textarea(attrs = {'cols' : 35 , 'rows' : 20 , 'id' : 'newstext' ,}),
		}
