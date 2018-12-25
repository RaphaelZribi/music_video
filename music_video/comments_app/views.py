from django.shortcuts import render
from django.http import HttpResponse
from comments_app.models import Comment
from identification_app.models import Profile
from main_app.models import Video, Playlist
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
import datetime
import json




#@csrf_exempt
def post_comment(request):
	user_profile = Profile.objects.get(user=request.user)
	date = datetime.datetime.now()

	if request.method == 'POST':
		video_id=request.POST.get('video_id')
		video = Video.objects.get(video_id=video_id)
		text = request.POST.get('text')
		comment = Comment(userprofileinfo=user_profile,video=video,text=text,date=date)
		comment.save()
		# all_comments = Comment.objects.all()
		# all_comments_list = []

		# for comment in all_comments:
		object_comment = {
			'username': comment.userprofileinfo.user.username,
			'text': comment.text,
			'date':  comment.date,
			'video':comment.video.video_id
		}

		#	all_comments_list.append(object_comment)

		response = {
			'code': 200,
			'comment': object_comment
		}

		return JsonResponse(response)

	else:
		error = { 'error': 'NOn Post methond not allowed'}
		return HttpResponse(json.dumps(error), content_type="application/json")

