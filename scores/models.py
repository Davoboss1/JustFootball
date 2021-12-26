from django.db import models
from django.forms import ModelForm , widgets
from standings.models import Table
from django.utils import timezone

# Create your models here.
class scores_date(models.Model):
	date = models.DateField(default = timezone.now(),unique=True)
	
	def __str__(self):
		return "Date : " + str(self.date)
	class Meta:
		app_label = 'scores'
		ordering = ['-date',]
		

class add_scores_date(ModelForm):
	class Meta:
		model = scores_date
		fields = ('date',)
		widgets = {
		'date' : widgets.DateInput(attrs={'type' : 'date'})
		}
	

class score(models.Model):
	date = models.ForeignKey(scores_date,on_delete=models.CASCADE)
	time = models.TimeField()
	league = models.ForeignKey(Table,on_delete=models.SET_NULL,null=True,blank=True)
	home = models.CharField(max_length=100)
	away = models.CharField(max_length= 100)
	home_score = models.IntegerField(null=True,blank=True)
	away_score = models.IntegerField(null=True,blank=True)
	home_team_id = models.IntegerField(null=True,blank=True,editable=False)
	away_team_id = models.IntegerField(null=True,blank=True,editable=False)
	
	
	def __str__(self):
		return str(self.date) + ' time - ' + str(self.time) + ' : ' + str(self.home) + ' ' + str(self.home_score) + ' - ' + str(self.away_score) + ' ' + str(self.away)
		
	class Meta:
		app_label = 'scores'
		ordering = ['date','time']

class add_score(ModelForm):
	class Meta:
		model = score
		fields = ('__all__')
		widgets = {
		'date' : widgets.Select(),
		'time' : widgets.TimeInput(attrs={'type' : 'time'}),
		'league' : widgets.Select(),
		'home' : widgets.TextInput(attrs={'id' : 'input_home'}),
		'away' : widgets.TextInput(attrs={'id' : 'input_away' }),
		'home_score' : widgets.NumberInput(attrs={'style' : 'width:8%;','type' : 'number' , 'id' : 'home_input_scores',}),
		'away_score' : widgets.NumberInput(attrs={'style' : 'width:8%;','type' : 'number' , 'id' : 'away_input_scores',}) ,
		}
	
	 	
class home_goal_scorers(models.Model):
	home_team = models.ForeignKey(score,on_delete=models.CASCADE)
	first_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	second_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	third_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	fourth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	fifth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	sixth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	seventh_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	eighth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	nineth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	tenth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	eleventh_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	twelfth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	thirteenth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	fourteenth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	fifteenth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	sixteenth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	seventeenth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	eighteenth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	nineteenth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	twentieth_home_scorer = models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return 'home : ' + str(self.home_team.home)
	class Meta:
		app_label = 'scores'
		
class add_home_goal_scorers(ModelForm):
	class Meta:
		model = home_goal_scorers
		fields = ('first_home_scorer','second_home_scorer','third_home_scorer','fourth_home_scorer','fifth_home_scorer','sixth_home_scorer','seventh_home_scorer','eighth_home_scorer','nineth_home_scorer','tenth_home_scorer','eleventh_home_scorer','twelfth_home_scorer','thirteenth_home_scorer','fourteenth_home_scorer','fifteenth_home_scorer','sixteenth_home_scorer','seventeenth_home_scorer' ,'eighteenth_home_scorer' ,'nineteenth_home_scorer','twentieth_home_scorer',)
		widgets = {
		'__all__' : widgets.TextInput(attrs={'style' : 'width:100%;',}),
	
		}
		
	
class away_goal_scorers(models.Model):
	away_team = models.ForeignKey(score,on_delete=models.CASCADE)
	first_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	second_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	third_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	fourth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	fifth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	sixth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	seventh_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	eighth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	nineth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	tenth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	eleventh_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	twelfth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	thirteenth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	fourteenth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	fifteenth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	sixteenth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	seventeenth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	eighteenth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	nineteenth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	twentieth_away_scorer = models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return 'away : ' + str(self.away_team.away)
		
	class Meta:
		app_label = 'scores'
		
	
class add_away_goal_scorers(ModelForm):
	class Meta:
		model = away_goal_scorers
		fields = ('first_away_scorer','second_away_scorer','third_away_scorer','fourth_away_scorer','fifth_away_scorer','sixth_away_scorer','seventh_away_scorer','eighth_away_scorer','nineth_away_scorer','tenth_away_scorer','eleventh_away_scorer','twelfth_away_scorer','thirteenth_away_scorer','fourteenth_away_scorer','fifteenth_away_scorer','sixteenth_away_scorer','seventeenth_away_scorer' ,'eighteenth_away_scorer' ,'nineteenth_away_scorer','twentieth_away_scorer',)
		
		widgets ={'__all__' : widgets.TextInput(attrs={'style':'width:100%'}),
		}
	
	
	
	
	
	
	
	
	
	
	
