from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^sobre/', views.about), 
	url(r'^contato/', views.contact, name='contact'), 
	#url(r'^bolos/', views.cakes, name='cakes'),
	#url(r'^produto/(?P<pk>[0-9]+)/$', views.product, name='product'),
]