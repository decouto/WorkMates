from django.db import models
from django.contrib.auth.models import User

class UserProjectManager(models.Manager):
	def create_project(self,name,date):
		project = self.create(name=name)
		pub_date = date
		return project

class UserProject(models.Model):
	pub_date = models.DateField('date published')
	project_name = models.CharField(max_length=200)
	keyImage = models.ImageField()
	creator = models.ForeignKey(User)
	def __unicode__(self):
		return project_name + " by " + creator.username

# How do we have more than one image per page?
class ProjectPage(models.Model):
	project = models.ForeignKey(Project)
	page_num = models.IntegerField()
	page_text = models.TextField()
	page_image = models.ImageField()
	def __unicode__(self):
		return project.project_name + "page: " + self.page_num

