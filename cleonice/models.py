from django.db import models
#from django.utils import timezone
#from cloudinary.models import CloudinaryField


class Product(models.Model):
	PRODUCT_TYPE = (
		('BO', 'Bolo'),
		('BI', 'Biscoito'),
	)

	name = models.CharField()

	def __str__ (self):
		return self.name