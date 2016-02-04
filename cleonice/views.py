from django.shortcuts import render

def index(request):
	title = "Home"
	return render(request, 'index.html', {'title': title})
