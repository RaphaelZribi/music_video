from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
	path('', views.index, name='index'),
	#path('video/<int:video_id>/', views.click_video, name='click_video'),


]