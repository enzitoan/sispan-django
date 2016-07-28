from django.contrib import admin

from .models import Detalle, Pan

class DetalleAdmin(admin.ModelAdmin):
	list_display = (
		'nombre',
		'email',
		'fecha_pedido', 
		'fecha_entrega', 
		'cantidad_pita_integral',
		'cantidad_pita_blanco', 
		'cantidad_amasado_integral',
		'cantidad_amasado_blanco'
	)

	list_filter = (
		'fecha_entrega',
	)

	fields = (
		'cantidad_pita_integral',
		'cantidad_pita_blanco', 
		'cantidad_amasado_integral',
		'cantidad_amasado_blanco'
	)

class PanAdmin(admin.ModelAdmin):
	list_display =  (
		'codigo',
    	'nombre',
    	'descripcion',
    	'valor',
	)
admin.site.register(Pan, PanAdmin)
admin.site.register(Detalle, DetalleAdmin)
