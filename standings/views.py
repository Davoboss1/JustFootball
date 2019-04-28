from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.views.generic import *
from django.utils.text import slugify
from home import views


	


def standings(request,league_url):

	
	
	Tables = Table.objects.get(url = league_url)
	Standing = Tables.standings_set.order_by('-points','-gd','position')
#	standing = Standings.objects.get(pk=1)
#	standing = Standings.objects.get(league.leagues_tabl,e = league_name)
	context = {'tables' : Tables,
	'standings' : Standing,
		}
	
	return render(request, 'standings/standings.html' , context)
