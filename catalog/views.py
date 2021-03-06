from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Category, ProductImage


class ProductListView(generic.ListView):
    """
    Lista TODOS os produtos
    """
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 10



class CategoryListView(generic.ListView):
    """
    Lista os produtos de determinada categoria (Bolo ou Biscoitos)
    """
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 10

    def get_queryset(self):
        """ Busca os produtos com a imagem (prefetch_related)"""
        return Product.objects.prefetch_related('images').filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


def product(request, slug):
    product = Product.objects.get(slug=slug)
    images = product.images.all()
    context = {
        'product': product,
        'images': "ROBINHO"
    }
    return render(request, 'catalog/product.html', context)


product_list = ProductListView.as_view()
category = CategoryListView.as_view()