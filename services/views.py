from django.http import HttpResponse

def ordered_features(request):
	return HttpResponse("This is the ordered features that you're looking for.")