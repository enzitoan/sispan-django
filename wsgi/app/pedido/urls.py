from django.conf.urls import url, include

from .views import *


urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^agregar/', agregar, name='agregar'),
	url(r'^guardar/', guardar, name='guardar'),
	url(r'^item/(?P<id>\d+)/', detalle, name='detalle'),
	url(r'^eliminar/(?P<id>\d+)/', eliminar, name='eliminar'),
	url(r'^pedido/', pedido, name='pedido'),
]