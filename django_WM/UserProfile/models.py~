from django.db import models
from django.contrib.auth.models import User

class UserProfileManager(models.Manager):
	def create_profile(self,user):

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	picture = models.ImageField()
	about_me = models.CharField(max_length = 200)
	interests = models.CharField(max_length = 200)
	locations = models.CharField(max_length = 200)

