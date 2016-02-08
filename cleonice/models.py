from django.db import models
#from django.utils import timezone
from cloudinary.models import CloudinaryField


class Product(models.Model):
	PRODUCT_TYPE = (
		('BO', 'Bolo'),
		('BI', 'Biscoito'),
	)

	name = models.CharField(max_length=200, null=False)
	#description = models.TextField('Descrição')
	#price = models.DecimalField(decimal_places=2, max_digits=10)
	#published_date = models.DateTimeField(auto_now_add=True)
	#product_type = models.CharField(max_length=2, choices=PRODUCT_TYPE, default='BO')

	def __str__ (self):
		return self.name


"""
class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = CloudinaryField('imagem', blank=True, null=True)
	description = models.CharField('Descrição', max_length=200, null=True)

	def __str__ (self):
		return self.product.name

"""