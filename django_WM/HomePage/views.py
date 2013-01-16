from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render

def index(request):
	template = loader.get_template('HomePage/index.html')
	context = Context({
		'css.css': 'HomePage/css.css',
		'main.jpg': 'HomePage/main.jpg',
		'banner.jpg':'HomePage/banner.jpg',
	})
	return HttpResponse(template.render(context))
