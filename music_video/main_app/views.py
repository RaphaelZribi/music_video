from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Playlist, Video


# Create your views here.

def home(request):
	playlists = Playlist.objects.all()
	print(playlists)
	videos = Video.objects.all()

	return render(request, 'home.html', { 'playlists': playlists, 'videos': videos})


#def click_video(request video_id):
#	video = Video.objects.get(video_id=video_id)
#	return render (request, 'main_app/click_video.html', {'video':video})
