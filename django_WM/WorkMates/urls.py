from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$',include('HomePage.urls')),
    	url(r'^admin/', include(admin.site.urls)),
	url(r'^projects/',include('UserProject.urls')),
	url(r'^search/',include('haystack.urls')),
	
)
