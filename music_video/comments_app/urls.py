from django.urls import path
from . import views

app_name = 'comments_app'

urlpatterns = [
	path('post_comment/', views.post_comment, name='post_comment'),

	#path('get_all_comments/<video_id>/', views.get_all_comments, name='get_all_comments'),



]