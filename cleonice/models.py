from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class IndexMediaCarrousel(models.Model):
	carrousel_title = models.CharField('Titulo carrousel', max_length=200)
	carrousel_substitle = models.CharField('Substitulo carrousel', max_length=200)
	carrousel_image = CloudinaryField('Carrousel')
	slide_active = models.BooleanField('Ativo', default=False)
	published_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.carrousel_title	


class IndexMediaCircle(models.Model):
	circle_title = models.CharField('Titulo circulo', max_length=200)
	circle_substitle = models.CharField('Substitulo circulo', max_length=200)
	circle_image = CloudinaryField('Imagem circulo')
	published_date = models.DateTimeField(auto_now_add=True)	

	def __str__(self):
		return self.circle_title


class IndexMediaPhotoFeatured(models.Model):
	photo_featured_title = models.CharField('Titulo imagem destaque', max_length=200)
	photo_featured_title_silver = models.CharField('Titulo cinza', max_length=200, default='')
	photo_featured_substitle = models.CharField('Substitulo imagem destaque', max_length=200)
	photo_featured_image = CloudinaryField('Foto destaque')
	published_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.photo_featured_title

	
