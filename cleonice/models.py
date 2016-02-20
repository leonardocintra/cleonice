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

	class Meta:
		ordering = ['product_name']


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = CloudinaryField('Imagem', blank=True, null=True)
	description = models.CharField('Descrição', max_length=200, null=True)

	def __str__ (self):
		return self.product.product_name


class IndexMediaCarrousel(models.Model):
	ORDER_SLIDE = (
		('FS', 'first-slide'),
		('SS', 'second-slide'),
		('TS', 'third-slide'),
	)

	carrousel_title = models.CharField('Titulo carrousel', max_length=200)
	carrousel_substitle = models.CharField('Substitulo carrousel', max_length=200)
	carrousel = CloudinaryField('Carrousel')
	order_slide = models.CharField('Ordem slide', choices=ORDER_SLIDE, unique=True, max_length=2)
	slide_active = models.BooleanField('Ativo', default=False)
	published_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.carrousel_title	


class IndexMediaCircle(models.Model):
	circle_title = models.CharField('Titulo circulo', max_length=200)
	circle_substitle = models.CharField('Substitulo circulo', max_length=200)
	circle = CloudinaryField('Imagem circulo')
	published_date = models.DateTimeField(auto_now_add=True)	

	def __str__(self):
		return self.circle_title


class IndexMediaPhotoFeatured(models.Model):
	photo_featured_title = models.CharField('Titulo imagem destaque', max_length=200)
	photo_featured_substitle = models.CharField('Substitulo imagem destaque', max_length=200)
	photo_featured = CloudinaryField('Foto destaque')
	published_date = models.DateTimeField(auto_now_add=True)	

	def __str__(self):
		return self.photo_featured_title

	
