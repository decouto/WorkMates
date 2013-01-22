from django.db import models
from django.contrib.auth.models import User
from AndTag.models import AndTag
from AtTag.models import AtTag
import tagging

class UserProfileManager(models.Manager):
	def create_profile(self,user):
		pass
# How do we associate projects with a specific profile?
class UserProfile(models.Model):
	user = models.OneToOneField(User)
#	picture = models.ImageField()
	about_me = models.CharField(max_length = 200)
	atLocation = models.ManyToManyField(AtTag) # For now projects can only have one location
	
tagging.register(UserProfile, tag_descriptor_attr = 'andTags')
