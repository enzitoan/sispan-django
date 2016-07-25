from django.contrib import admin

from .models import Region, Provincia, Comuna, Pan

class PanAdmin(admin.ModelAdmin):
	list_display = ['tipo']

class RegionAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nombre']
	search_fields = ('nombre',)

class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nombre']
	search_fields = ('nombre',)
	list_per_page = 15

class ComunaAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nombre']
	search_fields = ('nombre',)
	list_per_page = 15

admin.site.register(Pan, PanAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Comuna, ComunaAdmin)
