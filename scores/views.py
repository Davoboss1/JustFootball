from django.shortcuts import render , redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import QueryDict
from django.http import HttpResponse
from .models import *
from django.urls import reverse,reverse_lazy
from standings.models import Table,Standings
from home.views import Http_404 as error
from django.views.generic import WeekArchiveView,CreateView,UpdateView,DeleteView
# Create your views here.
class scores(WeekArchiveView):
	
	queryset = scores_date.objects.all()
	date_field = "date"
	context_object_name = "score"
	template_name = "scores/scores_page.html"
	week_format = "%W"
	allow_empty = True
	allow_future = True
	table = Table.objects.all()
	extra_context = {'table' : table,}
	

def add_scores_dates(request):
	form = add_scores_date()

	if request.method == 'POST':
		form = add_scores_date(request.POST)
		if form.is_valid():
			form.save()
			
			return redirect(reverse('scores:add_scores'))
	
	context = {'form' : form, 'error' : error, }
	return render(request,'scores/scores_date.html',context)

class add_scores(CreateView):
	form_class = add_score
	model = score
	
	
	extra_context = {'table' : Table.objects.all(),'error' : error}
	template_name = 'scores/scores_update.html'
	def form_valid(self,form):
		print(self.request.POST)

		Score = form.save(commit = False)
		if self.request.POST.get('home_input_id').isdigit() and self.request.POST.get('away_input_id'):
			home_id = int(self.request.POST.get('home_input_id'))
			away_id = int(self.request.POST.get('away_input_id'))
			Score.home_team_id = home_id
			Score.away_team_id = away_id
		
		Score.save()
		try:
			home_team = Standings.objects.get(id=home_id)
			away_team = Standings.objects.get(id=away_id)
			print(home_team.team)
			print(away_team.team)
			home_score = int(self.request.POST.get('home_score'))
			away_score = int(self.request.POST.get('away_score'))
			print("Home score :" , home_score , "away_score :" , away_score)
			if home_score > away_score:
				home_team.points += 3
				away_team.points += 0
				home_team.wins += 1
				away_team.losses+= 1
				home_team.gf += home_score
				home_team.ga += away_score
				home_team.gd = home_team.gf - home_team.ga
				away_team.gf += away_score
				away_team.ga += home_score
				away_team.gd = away_team.gf - away_team.ga
			
			elif away_score > home_score:
				away_team.points += 3
				home_team.points += 0
				away_team.wins += 1
				home_team.losses+= 1
				home_team.gf += home_score
				home_team.ga += away_score
				home_team.gd = home_team.gf - home_team.ga
				away_team.gf += away_score
				away_team.ga += home_score
				away_team.gd = away_team.gf - away_team.ga
			
			elif home_score == away_score:
				home_team.points += 1
				away_team.points += 1
				home_team.draws += 1
				away_team.draws += 1
				home_team.gf += home_score
				home_team.ga += away_score
				home_team.gd = home_team.gf - home_team.ga
				away_team.gf += away_score
				away_team.ga += home_score
				away_team.gd = away_team.gf - away_team.ga
			elif home_score == None or away_score == None:
				pass
		
			home_team.save()
			away_team.save()
			
		except (UnboundLocalError,ValueError):
			print("Error")
			
				
		
				
			
		
		
		
		self.success_url = reverse_lazy('scores:goal_scorers',kwargs={'score_id' : Score.id ,})
		
		return super(add_scores,self).form_valid(form)


def goal_scorers(request,score_id):
	score_object = score.objects.get(id=score_id)
	
	
	add_home_scorers = add_home_goal_scorers()
	add_away_scorers = add_away_goal_scorers()
	if request.method == "POST":
		
		home_form = add_home_goal_scorers(request.POST)
		away_form = add_away_goal_scorers(request.POST)
		if home_form.is_valid and away_form.is_valid():
			home = home_form.save(commit=False)
			home.home_team = score_object
			away = away_form.save(commit=False)
			away.away_team = score_object
			home.save()
			away.save()
			return redirect(reverse('scores:add_scores'))
	
	
	context={'home_form' : add_home_scorers,'away_form' : add_away_scorers,'home_score' :
	score_object , 'away_score' : score_object,'error' : error ,}
	
	
	return render(request,'scores/goal_scorers.html',context)
	
	
	
def update_scores_url(request):
	template_name="scores/scores_update_select.html"
	scores = score.objects.all()
	context = {'scores' :scores, 'error' : error ,}
	return render(request,template_name,context)

		
	
	
class update_scores(UpdateView):
	form_class = add_score
	model = score
	template_name = "scores/scores_update.html"
	extra_context = {'error' : error }
	
	def form_valid(self,form):
		print(self.request.POST)
		print(self.get_object())
		print(self.get_object().home_team_id)
		try:
			home_id = self.get_object().home_team_id
			away_id = self.get_object().away_team_id
			print("Home id" , home_id)
			home_team = Standings.objects.get(id=home_id)
			away_team = Standings.objects.get(id=away_id)
			initial_home_score = self.get_object().home_score
			initial_away_score = self.get_object().away_score
		
			if initial_home_score > initial_away_score:
				home_team.points -= 3
				away_team.points -= 0
				home_team.wins -= 1
				away_team.losses -= 1
				home_team.gf -= initial_home_score
				home_team.ga -= initial_away_score
				home_team.gd = home_team.gf - home_team.ga
				away_team.gf -= initial_away_score
				away_team.ga -= initial_home_score
				away_team.gd = away_team.gf - away_team.ga
			
			elif initial_away_score > initial_home_score:
				away_team.points -= 3
				home_team.points -= 0
				away_team.wins -= 1
				home_team.losses -= 1
				home_team.gf -= initial_home_score
				home_team.ga -= initial_away_score
				home_team.gd = home_team.gf - home_team.ga
				away_team.gf -= initial_away_score
				away_team.ga -= initial_home_score
				away_team.gd = away_team.gf - away_team.ga
			
			elif initial_home_score == initial_away_score:
				home_team.points -= 1
				away_team.points -= 1
				home_team.draws -= 1
				away_team.draws -= 1
				home_team.gf -= initial_home_score
				home_team.ga -= initial_away_score
				home_team.gd = home_team.gf - home_team.ga
				away_team.gf -= initial_away_score
				away_team.ga -= initial_home_score
				away_team.gd = away_team.gf - away_team.ga
			elif home_score == None or away_score == None:
				pass
		
		
			home_score = int(self.request.POST.get('home_score'))
			away_score = int(self.request.POST.get('away_score'))
			if home_score > away_score:
				home_team.points += 3
				away_team.points += 0
				home_team.wins += 1
				away_team.losses+= 1
				home_team.gf += home_score
				home_team.ga += away_score
				home_team.gd = home_team.gf - home_team.ga
				away_team.gf += away_score
				away_team.ga += home_score
				away_team.gd = away_team.gf - away_team.ga
			
			elif away_score > home_score:
				away_team.points += 3
				home_team.points += 0
				away_team.wins += 1
				home_team.losses+= 1
				home_team.gf += home_score
				home_team.ga += away_score
				home_team.gd = home_team.gf - home_team.ga
				away_team.gf += away_score
				away_team.ga += home_score
				away_team.gd = away_team.gf - away_team.ga
			
			elif home_score == away_score:
				home_team.points += 1
				away_team.points += 1
				home_team.draws += 1
				away_team.draws += 1
				home_team.gf += home_score
				home_team.ga += away_score
				home_team.gd = home_team.gf - home_team.ga
				away_team.gf += away_score
				away_team.ga += home_score
				away_team.gd = away_team.gf - away_team.ga
			elif home_score == None or away_score == None:
				pass
		
			home_team.save()
			away_team.save()
			
		except ObjectDoesNotExist:
			pass
		
		return super(update_scores, self).form_valid(form)
	
	def get_success_url(self):
		
		score_object = self.get_object()
		return reverse_lazy('scores:goal_scorers',kwargs={'score_id' : score_object.pk ,})

def delete_scores_url(request):
	template_name="scores/scores_delete_select.html"
	scores = score.objects.all()
	context = {'scores' : scores , 'error' : error ,}
	return render(request,template_name,context)
	

class delete_scores(DeleteView):
	
	model = score
	extra_context = {'error' : error , }
	success_url = reverse_lazy('scores:delete_scores_url')

