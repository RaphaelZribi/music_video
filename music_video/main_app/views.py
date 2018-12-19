from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main_app.models import Playlist, Video
import json


# Create your views here.

def home(request):
	playlists = Playlist.objects.all()
	print(playlists)
	videos = Video.objects.all()
	return render(request, 'home.html', { 'playlists': playlists, 'videos': videos})


def video_page(request, video_id):
	video = Video.objects.get(id=video_id)
	return render (request, 'click_video.html', {'video':video})

def like_section(request):
	if request.method == 'POST':
		video_id = request.POST.get('video_id')
		is_liked = False
		if video_id.likes.filter(id=request.user.id).exists():
			video_id.likes.remove(request.user)
			is_liked = False
		else:
			video_id.likes.add(request.user)
			is_liked = True

		context = {
			'video_id': video_id,
			'is_liked': is_liked,
			'total_likes': video_id.total_likes
		}
		return HttpResponse(json.dumps(response_data), content_type='application/json')

	else:
		error = { 'error': 'Non POST method not allowed' }
		return HttpResponse(json.dumps(error), content_type='application/json')
