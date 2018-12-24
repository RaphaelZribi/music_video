from django.db import models
from identification_app.models import Profile
from django.contrib.auth.models import User

#from datetime import datetime
from django.core.validators import URLValidator
# from django.utils import timezone




class Category(models.Model):
	name = models.CharField(max_length=200)

class Playlist(models.Model):
	playlist_id = models.TextField(unique=True)
	title       = models.TextField()
	description = models.TextField()
	thumbnail   = models.TextField(validators=[URLValidator()])

	def __repr__(self):
		return "<{}>".format(self.title)

	def __str__(self):
		return "{}".format(self.title)

class Video(models.Model):
	video_id    = models.TextField()
	title       = models.TextField()
	description = models.TextField()
	thumbnail   = models.TextField(validators=[URLValidator()], default=None)
	playlist    = models.ForeignKey(Playlist, on_delete=models.CASCADE)
	like        = models.ManyToManyField(User, related_name='likes', blank=True)
	# date        = models.DateField()
	#category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
	userprofileinfo = models.ForeignKey(Profile, on_delete=models.CASCADE)
	text = models.TextField()
	# date = models.DateTimeField(default=timezone.now())
	video = models.ForeignKey(Video, on_delete=models.CASCADE)


	def __repr__(self):
		return "<Comment of {}>".format(self.userprofileinfo.user.username)

	def __str__(self):
		return "{}".format(self.userprofileinfo.user.username)
