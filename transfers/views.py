from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.
from django.core.paginator import Paginator


class transfers_league(generic.ListView):
	template_name = "transfers/transfers_page.html"
	context_object_name = "pages"
	
	league_name = League_name.objects.all()
		
	
	extra_context = {'league' : league_name}
	
	
	def get_queryset(self):
		transfer = Transfers.objects.all()
	
		paginator = Paginator(transfer,100)
		page = self.request.GET.get('page')
		print(self.request.GET)
		return paginator.get_page(page)
		
		
	
	
		
	



