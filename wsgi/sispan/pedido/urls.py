from django.conf.urls import url, include

from .views import *


urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^pedido/', pedido, name='pedido'),
	url(r'^detalle/(?P<id>\d+)/', detalle, name='detalle'),
	url(r'^eliminar/(?P<id>\d+)/', eliminar, name='eliminar'),
	url(r'^guardar_detalle/', guardar_detalle, name='guardar_detalle'),
]