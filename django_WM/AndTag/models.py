from django.db import models

class AndTag(models.Model):
	tag = models.CharField(max_length = 9)
	def __unicode__(self):
		return "&" + self.tag.lower()
