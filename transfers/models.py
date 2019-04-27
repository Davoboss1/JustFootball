from django.db import models

# Create your models here.
class League_name(models.Model):
	name_of_league = models.CharField(max_length = 250)
	
	def __str__(self):
		return self.name_of_league
	class Meta:
		app_label = 'transfers'
		

class Transfers(models.Model):
	league = models.ForeignKey(League_name,on_delete=models.CASCADE)
	date = models.DateField()

	Player_name = models.CharField(max_length=500)
	From = models.CharField(max_length=200)
	To = models.CharField(max_length=200)
	def __str__(self):
		return self.Player_name + " From " + self.From + " To " + self.To
		
	class Meta:
		app_label = 'transfers'
		verbose_name = "Transfer"
		ordering = ["-date"]
		



		
