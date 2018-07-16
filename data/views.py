from django.http import Http404
from django.shortcuts import render
from .models import Album 

# Create your views here.

def index(request):
	all_albums = Album.objects.all()
	return render(request, 'data/index.html', {'all_albums': all_albums})

def dashboard(request):
	all_albums = Album.objects.all()
	return render(request, 'data/dashboard2.html', {'all_albums': all_albums})


 
def detail(request, album_id):
	try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("No alerts")
	return render(request, 'data/detail.html', {'album': album})

	

