from django.db import models
from datetime import date
import datetime

# Create your models here.
class Pan(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=70)
    descripcion = models.TextField(max_length=100)
    valor = models.IntegerField()
    
class Detalle(models.Model):
    fecha_pedido = models.DateField(default=date.today())
    fecha_entrega = models.DateField(default=date.today())
    cantidad_pita_integral = models.IntegerField(default=0)
    cantidad_pita_blanco = models.IntegerField(default=0)
    cantidad_amasado_integral = models.IntegerField(default=0) 
    cantidad_amasado_blanco = models.IntegerField(default=0)
    nombre = models.CharField(max_length=120)
    email = models.EmailField()


