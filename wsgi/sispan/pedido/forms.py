from django import forms

from .models import Detalle

class DetalleForm(forms.ModelForm):

    class Meta:
        model = Detalle

        fields = [
            'cantidad_pita_blanco',
            'cantidad_pita_integral',
            'cantidad_amasado_blanco',
            'cantidad_amasado_integral',
            'nombre',
            'email',
        ]
        labels = {
            'cantidad_pita_blanco': 'Pita Blanco',
            'cantidad_pita_integral': 'Pita Integral',
            'cantidad_amasado_blanco': 'Amasado Blanco',
            'cantidad_amasado_integral': 'Amasado Integral',
            'nombre': 'Nombre Completo',
            'email': 'E-Mail',        
        }
        widgets = {
            'cantidad_pita_blanco': forms.NumberInput(
                attrs={
                    'id': 'txtPan1',
                    'class':'form-control txt-pedido',
                    'min': 1,
                    'required': True,
                    'disabled': True,
                }
            ),
            'cantidad_pita_integral': forms.NumberInput(
                attrs={
                    'id': 'txtPan2',
                    'class':'form-control txt-pedido',
                    'min': 1,
                    'required': True,
                    'disabled': True,
                }
            ),
            'cantidad_amasado_blanco': forms.NumberInput(
                attrs={
                    'id': 'txtPan3',
                    'class':'form-control txt-pedido',
                    'min': 1,
                    'required': True,
                    'disabled': True,
                }
            ),
            'cantidad_amasado_integral': forms.NumberInput(
                attrs={
                    'id': 'txtPan4', 
                    'class':'form-control txt-pedido',
                    'min': 1,
                    'required': True,
                    'disabled': True,
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'id': 'txtNombre',
                    'class':'form-control',
                    'required': True,                    
                    'disabled': True,
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'id': 'txtCorreo',
                    'class':'form-control',
                    'required': True,
                    'disabled': True,
                }
            ),
        }