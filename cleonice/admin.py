from django.contrib import admin
from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
	search_fields = ('product_name', )

admin.site.register(Product)
admin.site.register(ProductImage)