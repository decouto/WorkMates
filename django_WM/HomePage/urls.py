from django.conf.urls import patterns, url
from HomePage import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='HomePage_index'),


)
