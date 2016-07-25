from django.contrib import admin

from .models import Persona, Detalle, Direccion, Pan

class ItemAdmin(admin.ModelAdmin):
	list_display = [
		'titulo', 
		'cantidad',
	]

class PersonaAdmin(admin.ModelAdmin):
	list_display = [
		'rut', 
		'nombre', 
		'apellido_paterno', 
		'apellido_materno',
	]

class DetalleAdmin(admin.ModelAdmin):
	list_display = [
		'fecha_pedido', 
		'fecha_entrega', 
		'cantidad_pita_integral',
		'cantidad_pita_blanco', 
		'cantidad_amasado_integral',
		'cantidad_amasado_blanco',
	]

class DireccionAdmin(admin.ModelAdmin):
	list_display = [
		'persona',
		'calle',
		'numero',
	]

class PanAdmin(admin.ModelAdmin):
	list_display =  [
		'codigo',
    	'nombre',
    	'descripcion',
    	'valor',
	]
admin.site.register(Pan, PanAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Detalle, DetalleAdmin)
admin.site.register(Direccion, DireccionAdmin)
