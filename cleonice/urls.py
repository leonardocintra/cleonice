from django.conf.urls import url, include
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^sobre/', views.about), 
	url(r'^contato/', views.contact, name='contact'), 
	url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', admin.site.urls),
	#url(r'^bolos/', views.cakes, name='cakes'),
	#url(r'^produto/(?P<pk>[0-9]+)/$', views.product, name='product'),
]
