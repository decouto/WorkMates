from django.http import HttpResponse

def index(request):
	return HttpResponse("This is the home page. You found it.")
