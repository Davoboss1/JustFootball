from django.shortcuts import render, redirect
from django.urls import  reverse,reverse_lazy
from django.http import HttpResponse,Http404
from .models import football_posts , post_football
from home import views as error
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.

def news(request,no,title_url):
	posts = football_posts.objects.get(id = no,url = title_url)
	def home_goal_scorers_value(post):
		
		try:
			if post.match.home_goal_scorers_set.all().exists():
				goal_scorers = post.match.home_goal_scorers_set.all().values_list()
				goal_scorer = tuple(goal_scorers.first())
				return goal_scorer[2:]
			
		except AttributeError:
			pass
	
	def away_goal_scorers_value(post):
		try:
			if post.match.away_goal_scorers_set.all().exists():
				goal_scorers = post.match.away_goal_scorers_set.all().values_list()
				goal_scorer = tuple(goal_scorers.first())
				return goal_scorer[2:]
		except AttributeError:
			pass

		
	
	context = {'post' : posts ,'home_goal_scorers' : home_goal_scorers_value(posts) ,'away_goal_scorers' : away_goal_scorers_value(posts) ,}
		
	return render(request,"news/News_page.html",context)
	
	


class post_news(CreateView):
	form_class = post_football
	model = football_posts
	template_name = 'news/news_update.html'
	
	
	def form_valid(self,form):
		form.save()
		return super(post_news, self).form_valid(form)
	
	def get_success_url(self):
		
		
		return reverse("Homepage")
	extra_context = {'error' : error}
	
		
	
def update_news_url(request):
	template_name="news/news_update_select.html"
	posts = football_posts.objects.all()
	context = {'post' :posts ,'error' : error}
	return render(request,template_name,context)
	
	
	
	
class update_news(UpdateView):
	form_class = post_football
	model = football_posts
	template_name = "news/news_update.html"
	success_url = reverse_lazy("news:news_update")
	extra_context = {'error' : error}

def delete_news_url(request):
	template_name="news/news_delete_select.html"
	posts = football_posts.objects.all()
	context = {'post' :posts ,'error' : error}
	return render(request,template_name,context)
	

class delete_news(DeleteView):
	
	model = football_posts
	extra_context = {'error' : error}
	success_url = reverse_lazy('news:news_delete')




