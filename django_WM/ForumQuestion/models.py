
from django.db import models
from django.contrib.auth.models import User
import tagging

class ForumQuestionManager(models.Manager):
	def create_question(self):
		pass

class ForumQuestion(models.Model):
	question = models.CharField(max_length = 200)
	asker = models.ForeignKey(User)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question
	

class ForumAnswer(models.Model):
	question = models.ForeignKey(ForumQuestion)
	answer_text = models.TextField('ans_text')
	answerer = models.ForeignKey(User)
	def __unicode__(self):
		return self.answerer.username + ": " + self.question.question
