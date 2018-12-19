from django.db import models
from identification_app.models import Profile
#from datetime import datetime
from django.core.validators import URLValidator
# from django.utils import timezone




class Category(models.Model):
	name = models.CharField(max_length=200)

class Playlist(models.Model):
	playlist_id = models.CharField(max_length=400, unique=True)
	title       = models.CharField(max_length=400)
	description = models.CharField(max_length=400)
	thumbnail   = models.CharField(max_length=2000, validators=[URLValidator()])

	def __repr__(self):
		return "<{}>".format(self.title)

	def __str__(self):
		return "{}".format(self.title)

class Video(models.Model):
	video_id    = models.CharField(max_length=2000)
	title       = models.CharField(max_length=2000)
	description = models.CharField(max_length=2000)
	thumbnail   = models.CharField(max_length=2000, validators=[URLValidator()], default=None)
	playlist    = models.ForeignKey(Playlist, on_delete=models.CASCADE)
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
