from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from UserProject.models import UserProject

def index(request):
	return HttpResponse("The project index")

def detail(request,project_id):
	try:
		project = UserProject.objects.get(pk=project_id)
	except UserProject.DoesNotExist:
		raise Http404
	return render(request,'UserProject/detail.html',{'poll':poll})


