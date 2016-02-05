from django.shortcuts import render

def index(request):
	title = "Home"
	return render(request, 'index.html', {'title': title })

def contact(request):
	title = "Contato"
	return render(request, 'contato.html', {'title': title })

def about(request):
	title = "Sobre"
	return render(request, 'sobre.html', {'title': title })

def cake(request):
	title = "Bolos"
	return render(request, 'bolos.html', {'title': title })