from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Category


class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 10


class CategoryListView(generic.ListView):
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


product_list = ProductListView.as_view()
category = CategoryListView.as_view()