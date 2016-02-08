from django.test import TestCase
from .models import Product

class ProductTest(TestCase):
	def setUp(self):
		Product.objects.create(product_name="Bolo de Cenoura")
		Product.objects.create(product_name="Bolo de Fuba")
		Product.objects.create(product_name="Bolo de Morango")
