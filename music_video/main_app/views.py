from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('salut les gars')

#def click_video(request video_id):
#	video = Video.objects.get(video_id=video_id)
#	return render (request, 'main_app/click_video.html', {'video':video})