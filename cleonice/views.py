from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage

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

	return render(request, 'bolos.html', {
		'cakes': cakes, 
		'title': title 
	})

def product(request, pk):
	title = "Bolo"
	product = get_object_or_404(Product, pk=pk)
	photos = ProductImage.objects.all().filter(product=product.pk)

	return render(request, 'bolo.html', {
		'product': product, 
		'photos': photos,
		'title': title })

