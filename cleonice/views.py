from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
	title = "Home"
	return render(request, 'index.html', {'title': title })

def contact(request):
	title = "Contato"
	return render(request, 'contato.html', {'title': title })

def about(request):
	title = "Sobre"
	return render(request, 'sobre.html', {'title': title })

def cakes(request):
	title = "Bolos"
	cakes = Product.objects.all()
	return render(request, 'bolos.html', {'cakes': cakes, 'title': title })

def product(request, pk):
	title = "Bolo"
	prod = get_object_or_404(Product, pk=pk)
	return render(request, 'bolo.html', {'prod': prod, 'title': title })

