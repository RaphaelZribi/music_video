from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from main_app.models import Playlist, Video
from django.contrib.auth.decorators import login_required
from comments_app.forms import CommentForm
from comments_app.models import Comment
import json


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
	comment_form = CommentForm()
	comments = Comment.objects.filter(video=video)
	return render (request, 'click_video.html', {'video':video, 'comment_form':comment_form, 'comments':comments})



	is_liked = False
	if video.like.filter(id=request.user.id).exists():
		is_liked = True
	return render (request, 'click_video.html', {'video':video, 'is_liked':is_liked})

	
def like_section(request, video_id):
	"""If user has liked video, unlike it. Otherwise, like it."""
	print("#####")
	if request.method == 'POST':
		is_liked = False
		video = Video.objects.get(id=video_id)
		if video.like.filter(id=request.user.id).exists():
			video.like.remove(request.user)
			is_liked = False
		else:
			video.like.add(request.user)
			is_liked = True

		response_data = {
			'result': 'success',
			'is_liked': is_liked,
			# 'total_likes': video_id.total_likes
		}
		return HttpResponse(json.dumps(response_data), content_type='application/json')

	else:
		error = { 'error': 'Non POST method not allowed' }

		return HttpResponse(json.dumps(error), content_type='application/json')



			# video = get_object_or_404(Video, id=request.POST.get('video_id'))
	# is_liked = False
	# if video.like.filter(id=request.user.id).exists():
	# 	video.like.remove(request.user)
	# 	is_liked = False
	# else:
	# 	video.like.add(request.user)
	# 	is_liked = True


	# return redirect(reverse('main_app:video_page'))

