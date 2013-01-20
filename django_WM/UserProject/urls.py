from django.conf.urls import patterns, url
from UserProject import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='UserProject_index'),
	url(r'^(?P<project_id>\d+)/$', views.detail, name = 'UserProject_detail'),

)
