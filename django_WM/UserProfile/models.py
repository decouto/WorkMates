from django.db import models
from django.contrib.auth.models import User

class UserProfileManager:
	def create_profile(self,user):

class UserProfile:
	name = models.CharField(max_length = 50)
	picture = models.ImageField()
	about_me = models.CharField(max_length = 200)
	interests = models.CharField(max_length = 200)
	locations = models.CharField(max_length = 200)

