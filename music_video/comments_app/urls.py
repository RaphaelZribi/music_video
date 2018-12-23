from django.urls import path
from . import views

app_name = 'comments_app'

urlpatterns = [

	path('comment/', views.comment, name='comment'),



]