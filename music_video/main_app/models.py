from django.db import models
from django.contrib.auth.models import User



class Video(models.Model):
	

class Category(models.Model):

class Comment(models.Model):


class Profile(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
