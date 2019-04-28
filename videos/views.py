from django.shortcuts import render
from .models import Video
# Create your views here.
def Videos(request):
	videos = Video.objects.all()
	context = {
	'video' : videos
	}
	return render(request,"videos/Videos_page.html",context)
	