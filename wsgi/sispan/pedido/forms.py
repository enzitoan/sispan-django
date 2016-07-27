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
		labels = {
		    'cantidad_pita_integral': 'Pita Integral',
		    'cantidad_pita_blanco': 'Pita Blanco',
		    'cantidad_amasado_integral': 'Amasado Integral',
		    'cantidad_amasado_blanco': 'Amasado Blanco',
		    'nombre': 'Nombre Completo',
		    'email': 'E-Mail',		
		}
		widgets = {
			'cantidad_pita_integral': forms.TextInput(attrs={'class':'form-control txt-pedido'}),
			'cantidad_pita_blanco': forms.TextInput(attrs={'class':'form-control txt-pedido'}),
			'cantidad_amasado_integral': forms.TextInput(attrs={'class':'form-control txt-pedido'}),
			'cantidad_amasado_blanco': forms.TextInput(attrs={'class':'form-control txt-pedido'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
		}