from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [

	path('', views.home, name='home'),
	path('video/<int:video_id>/', views.video_page, name='video_page'),



]