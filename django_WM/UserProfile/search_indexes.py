from UserProfile.models import UserProfile
from haystack import indexes
import datetime

class UserProfileIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document = True, use_template= True)
	user = indexes.CharField(model_attr = 'user')
	atTags = indexes.CharField(model_attr = 'atTag')
	andTags = indexes.CharField(model_attr = 'andTags')

	def get_model(self):
		return UserProfile

	def index_queryset(self):
		return self.get_model().objects.filter(pub_date_lte = datetime.datetime.now())

