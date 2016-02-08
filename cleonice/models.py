from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Product(models.Model):
	PRODUCT_TYPE = (
		('BO', 'Bolo'),
		('BI', 'Biscoito'),
	)

	product_name = models.CharField('Nome', max_length=200)
	description = models.TextField('Descrição')
	price = models.DecimalField('Preço', decimal_places=2, max_digits=10)
	published_date = models.DateTimeField(auto_now_add=True)
	product_type = models.CharField('Tipo', max_length=2, choices=PRODUCT_TYPE, default='BO')

	def __str__ (self):
		return self.product_name


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = CloudinaryField('Imagem', blank=True, null=True)
	description = models.CharField('Descrição', max_length=200, null=True)

	def __str__ (self):
		return self.product.product_name
