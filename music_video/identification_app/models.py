from django.db import models
from django.contrib.auth.models import User
#from main_app.models import 
#from datetime import datetime
from django.core.validators import URLValidator

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

	def __repr__(self):
		return "<User: {}>".format(self.user.username)

	def __str__(self):
		return '{}'.format(self.user.username)
