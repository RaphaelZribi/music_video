from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Playlist, Video
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/identification_app/login')
def home(request):
	playlists = Playlist.objects.all()
	print(playlists)
	videos = Video.objects.all()
	return render(request, 'home.html', { 'playlists': playlists, 'videos': videos})

@login_required(login_url='/identification_app/login')
def video_page(request, video_id):
	video = Video.objects.get(id=video_id)
	return render (request, 'click_video.html', {'video':video})
