from django.http import HttpResponse

def index(request):
	return HttpResponse("This is the home page for WorkMates. You found it.")
