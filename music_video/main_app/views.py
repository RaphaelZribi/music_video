from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Playlist, Video


# Create your views here.
def home(request):
	playlists = Playlist.objects.all()
	print(playlists)
	# videos = Video.objects.all().order_by('-date')[:10]

	return render(request, 'home.html', { 'playlists': playlists})
