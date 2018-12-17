from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Video(models.Model):
	title = models.CharField(max_length=400)
	url = models.CharField(max_length=2000, validators=[URLValidator()])
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Category(models.Model):
	name = models.CharField(max_length=200)

class Comment(models.Model):
	userprofileinfo = models.ForeignKey(Profile, on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateTimeField(default=datetime.now())
	video = models.ForeignKey(Video, on_delete=models.CASCADE)


	def __repr__(self):
		return "<Comment of {}>".format(self.userprofileinfo.user.username)

	def __str__(self):
		return "{}".format(self.userprofileinfo.user.username)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=500)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

	def __repr__(self):
		return "<User: {}>".format(self.user.username)

	def __str__(self):
		return '{} {}'.format(self.user.first_name, self.user.last_name)

