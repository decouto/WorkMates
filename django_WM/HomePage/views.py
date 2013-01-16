from django.http import HttpResponse

def index(request):
	c = {}
	return render_to_response('index.html', c)
