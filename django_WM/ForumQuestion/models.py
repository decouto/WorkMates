from django.db import models
from django.contrib.auth.models import User

class ForumQuestionManager(models.Manager):
	def create_question(self):

class Question(models.Model):
	question = models.CharField(max_length = 200)
	asker = models.ForeignKey(User)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question
	

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.TextField()
	answerer = models.ForeignKey(User)
	def __unicode__(self):
		return self.answerer.self.username + ": " + question
