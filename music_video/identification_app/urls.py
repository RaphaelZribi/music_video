from django.urls import path
from . import views

app_name = 'identification_app'

urlpatterns = [

	path('login/', views.log_in, name='loginpage'),
	path('signup/', views.signup, name='signup'),
	
]