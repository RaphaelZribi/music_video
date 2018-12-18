from django.db import models
from django.contrib.auth.models import User
#from datetime import datetime
from django.core.validators import URLValidator
from django.utils import timezone




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
	video_id    = models.CharField(max_length=2000, unique=True)
	title       = models.CharField(max_length=2000)
	description = models.CharField(max_length=2000)
	thumbnail   = models.CharField(max_length=2000, validators=[URLValidator()], default=None)
	playlist    = models.ForeignKey(Playlist, on_delete=models.CASCADE)
	#category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=500)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

	def __repr__(self):
		return "<User: {}>".format(self.user.username)

	def __str__(self):
		return '{} {}'.format(self.user.first_name, self.user.last_name)


class Comment(models.Model):
	userprofileinfo = models.ForeignKey(Profile, on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now())
	video = models.ForeignKey(Video, on_delete=models.CASCADE)


	def __repr__(self):
		return "<Comment of {}>".format(self.userprofileinfo.user.username)

	def __str__(self):
		return "{}".format(self.userprofileinfo.user.username)
