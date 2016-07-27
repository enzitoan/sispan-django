from django.conf.urls import url, include

from .views import *

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^pedido/', pedido, name='pedido'),
	url(r'^listado/', pedido_listado, name='pedido_listado'),
	url(r'^editar/(?P<id>\d+)/$', pedido_editar, name='pedido_editar'),
	url(r'^eliminar/(?P<id>\d+)/$', pedido_eliminar, name='pedido_eliminar'),
]