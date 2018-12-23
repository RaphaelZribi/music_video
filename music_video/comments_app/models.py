from django.db import models
from identification_app.models import Profile
from main_app.models import Playlist, Video


class Comment(models.Model):
	userprofileinfo = models.ForeignKey(Profile, on_delete=models.CASCADE)
	video = models.ForeignKey(Video, on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateTimeField()


	def __repr__(self):
		return "<Comment of {}>".format(self.userprofileinfo.user.username)

	def __str__(self):
		return "{}".format(self.userprofileinfo.user.username)