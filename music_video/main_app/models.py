from django.db import models
from identification_app.models import Profile
from django.core.validators import URLValidator

class Category(models.Model):
	name = models.TextField()

class Playlist(models.Model):
	playlist_id = models.TextField()
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
	# date        = models.DateField()
	#category = models.ForeignKey(Category, on_delete=models.CASCADE)


	def __repr__(self):
		return "<{}>".format(self.title)

	def __str__(self):
		return "{}".format(self.title)

