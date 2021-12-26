from django.db import models
from django.forms import ModelForm , widgets
from django.utils.text import slugify
# Create your models here.



		

# Table for all Leagues

class Table(models.Model):
	#team contains all teams in all leagues
	continent = models.CharField(max_length =30)
	leagues_table = models.CharField(max_length = 200)
	url = models.SlugField(max_length = 200,default = "url",editable=False)
	def save(self,*args,**kwargs):
		self.url = slugify(self.leagues_table,allow_unicode=True)
		
		
		
		super(Table, self).save(*args, **kwargs) 
		
	def __str__(self):	
		return self.continent + ' - ' + self.leagues_table 

class Table_name(ModelForm):
	class Meta:
		model = Table
		fields = ('leagues_table',)
		widgets = {
		'leagues_table' : widgets.TextInput(attrs={
	'name' : 'league_name',
	'type' : 'text',
	'class' : 'form-control',
	'style' : 'height : 1px; width:90%; margin-top : 25px; margin-left:2%;',
	'placeholder' : 'Enter Leagues',
	'autocomplete' : 'on',
	'id' : 'myInput' ,
}), }
	
	


#for competitions in europe
class europe_competitions(models.Model):
	europe_competition = models.ForeignKey(Table,on_delete=models.CASCADE,)
	
	#competitions = europe_competition
	
	
	
	def __str__(self):
		return self.europe_competition.leagues_table
	
#for competitions in africa
class africa_competitions(models.Model):
	
	africa_competition = models.ForeignKey(Table,on_delete=models.CASCADE,)
	
	
	def __str__(self):
		return self.africa_competition.leagues_table

#for competitions in north america
class north_america_competitions(models.Model):
	
	north_america_competition = models.ForeignKey(Table,on_delete=models.CASCADE,)
	
	
	def __str__(self):
		return self.north_america_competition.leagues_table

#for competitions in south america
class south_america_competitions(models.Model):
	south_america_competition = models.ForeignKey(Table,on_delete=models.CASCADE,)
	
	
	def __str__(self):
		return self.south_america_competition.leagues_table


#for competitions in asia
class asia_competitions(models.Model):
	
	asia_competition = models.ForeignKey(Table,on_delete=models.CASCADE,) 
	
	def __str__(self):
		return self.asia_competition.leagues_table

#for competitions in australia
class australia_competitions(models.Model):
	
	australia_competition = models.ForeignKey(Table,on_delete=models.CASCADE,)
	
	
	def __str__(self):
		return self.australia_competition.leagues_table


#for any other competitions 
class others_competitions(models.Model):
	
	others_competition = models.ForeignKey(Table,on_delete=models.CASCADE,)
	
	
	def __str__(self):
		return self.others_competition.leagues_table


	
	
#Table Data
class Standings(models.Model):
	position = models.IntegerField(null = True,blank=True)
	league_name = models.ForeignKey(Table,on_delete=models.CASCADE,)
	team = models.CharField(max_length = 50,default = "Team")
	points = models.IntegerField(default = 0)
	wins = models.IntegerField(default = 0)
	draws = models.IntegerField(default =0)
	losses = models.IntegerField(default=0)
	gf = models.IntegerField(default =0)
	ga = models.IntegerField(default= 0)
	gd = models.IntegerField(default = 0)

	
	def __str__(self):
		return "{} {} pts - {}".format( self.league_name.leagues_table, self.team,str(self.points))
		
		
	class Meta:
		verbose_name = "Standing"
		
		ordering = ['league_name','-points']
		
		
		
