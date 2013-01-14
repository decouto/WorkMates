from django.db import models
from django.contrib.auth.models import User

class UserProjectManager(models.Manager):
	def create_project(self,name,date):
		project = self.create(name=name)
		pub_date = date
		return project

class UserProject(models.model):
	pub_date = models.DateField()
	name = models.CharField(max_length=200)
	textContent = models.TextField()
	imageContent = models.ImageField()


