from django.contrib import admin
from .models import Product, ProductImage, IndexMediaCarrousel, IndexMediaCircle, IndexMediaPhotoFeatured

class ProductAdmin(admin.ModelAdmin):
	search_fields = ('product_name', )

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(IndexMediaCarrousel)
admin.site.register(IndexMediaCircle)
admin.site.register(IndexMediaPhotoFeatured)