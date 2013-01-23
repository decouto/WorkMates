from userProject.models import UserProject
from haystack import indexes
import datetime

class UserProjectIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document = True, use_template= True)
	author = indexes.CharField(model_attr = 'creator')
	pub_date = indexes.DateTimeField(model_attr = 'pub_date')
	atTags = indexes.CharField(model_attr = 'atTag')
	andTags = indexes.CharField(model_attr = 'andTags')
	name = indexes.CharField(model_attr = 'project_name')

	def get_model(self):
		return UserProject

	def index_queryset(self):
		return self.get_model().objects.filter(pub_date_lte = datetime.datetime.now())

