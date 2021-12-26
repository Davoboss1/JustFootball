from django.shortcuts import render , redirect
from transfers.models import Transfers
from django.urls import reverse
from django.utils import timezone
from datetime import date 
from django.http import HttpResponse ,Http404
from django.views import generic
from django.core.paginator import Paginator
from .models import slider
from news.models import football_posts
# Create your views here.
from scores.models import score , scores_date
from standings.models import *
from videos.models import Video
import time
from django.http import QueryDict
from justfootball import settings
from django.contrib.auth import authenticate,login
from django.contrib import messages
'''
class news(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'news'
	
	def get_queryset(self):
		return football_posts.objects.all()
		
class standing(generic.ListView):
	
	
	template_name = 'home/index.html'
	context_object_name = 'europe_comps'
	def get_queryset(self):
		return europe_competitions.objects.all()
	
	
'''
def control_panel(request):
	if request.user.is_authenticated:
		return render(request,'home/control_panel.html',{})
	else:
		raise Http404("Page does not exist")

def login_view(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("control_panel")
		else:
			messages.error(request,"Username or password incorrect.")
	return render(request,"home/login.html",{})
	
def homepage(request):
	show  = str()
	Slider = slider.objects.all()
	league_name = None
	Tables = Table.objects.all()
	table_name = Table_name()
	#All football news posts
	all_posts = football_posts.objects.all()
	
	paginator = Paginator(all_posts,15)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	
	
	
	#All scores 
	
	scores_object = scores_date.objects.filter(date = date.today())
	
	print(scores_object)
	
	#All european competitions 
	europe_comp = europe_competitions.objects.all()

  
  #All African competitions 
	africa_comp = africa_competitions.objects.all()
	#All North America competitions 
	north_america_comp = north_america_competitions.objects.all()

	#All South America competitions 
	south_america_comp = south_america_competitions.objects.all()
	#All Asian competitions 
	asia_comp = asia_competitions.objects.all()
	#All australian competitions 
	australia_comp = australia_competitions.objects.all()
	#All Other competitions 
	others_comp = others_competitions.objects.all()

	if request.method == 'GET':
		form = Table_name(request.GET)
		
		print(request.GET)
		if form.is_valid():
			show = request.GET.copy()
			show.__setitem__("class", "in")
			show = show['class']
			print("Valid" , show)
		
			league_name = Table.objects.filter(leagues_table__contains = request.GET.get('leagues_table'))
			
		if request.GET.__contains__("search"):
			print("It contains")
			search = str(request.GET.get("search"))
			searched_post = football_posts.objects.filter(Title__contains = search) | football_posts.objects.filter(summary__contains = search) | football_posts.objects.filter(news__contains = search) 
	
			paginators = Paginator(searched_post,15)
			page = request.GET.get('page')
			post = paginators.get_page(page)
	
			searched_scores = score.objects.filter(home__contains = search) | score.objects.filter(away__contains = search)
			scores_paginator = Paginator(searched_scores,20)
			pages = request.GET.get('pages')
			scores_pages = scores_paginator.get_page(pages)
	
			searched_standings = Standings.objects.filter(team__contains = search) 
			searched_league = Table.objects.filter(leagues_table__contains = search) 
		
			searched_transfer = Transfers.objects.filter(From__contains = search) | Transfers.objects.filter(To__contains = search)
			searched_Videos = Video.objects.filter(video_name__contains = search)
			print(searched_standings)
			context = {}
		
			context['news'] = post
			context['all_posts'] = searched_post
			context['search'] = search
			context['total_pages'] = paginators.num_pages
			context['searched_scores'] = searched_scores
			context['scores'] = scores_pages
		
	
			context['standing'] = searched_standings
			context['table'] = searched_league
			context['transfers'] = searched_transfer
			context['video'] = searched_Videos
			return render(request,'home/search.html',context)
	
			
	
	print(league_name)
	
	
	contexts = {'news' : posts ,
	'total_pages' : paginator.num_pages ,
'score' : scores_object ,
'europe_comps' : europe_comp,
'africa_comps' : africa_comp,
'north_america_comps' : north_america_comp ,
'south_america_comps' : south_america_comp ,
'asia_comps' : asia_comp,
'australia_comps' : australia_comp,
'others_comps' : others_comp,
'tables' : Tables ,
'league_search_result' : league_name,
'video' : Video.objects.all(),
'date' : time.strftime("%Y/%W",time.gmtime())
,'league_name' : table_name ,
'in' : show,
'slider' : Slider,
}
	
	
	return render(request,'home/index.html',contexts)


def Http_404():
	raise Http404("Page does not exist")