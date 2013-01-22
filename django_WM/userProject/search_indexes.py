from UserProject import UserProject
from haystack import indexes
import datetime

class UserProjectIndex(indexes.SearchIndex, indexes.Indexeable):
	text = indexes.CharField(document = True, use_template= True)
	author = indexes.CharField(model_attr = 'creator')
	pub_date = indexes.DateTimeField(model_attr = 'pub_date')
	atTag = indexes.CharField(model_attr = 'atTag')
	andTag = indexes.CharField(model_attr = 'andTag')
	name = indexes.CharField(model_attr = 'project_name')

	def get_model(self):
		return UserProject

	def index_queryset(self):
		return self.get_model().objects.filter(pub_date_lte = datetime.datetime.now())
