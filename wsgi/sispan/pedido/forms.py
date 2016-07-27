from django import forms

from .models import Detalle

class DetalleForm(forms.ModelForm):

	class Meta:
		model = Detalle

		fields = [
		    'cantidad_pita_integral',
		    'cantidad_pita_blanco',
		    'cantidad_amasado_integral',
		    'cantidad_amasado_blanco',
		    'nombre',
		    'email',
		]