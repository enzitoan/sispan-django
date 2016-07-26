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

    def next_weekday(d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0: # Target day already happened this week
            days_ahead += 7
        return d + datetime.timedelta(days_ahead)

    pedido = date.today
    entrega = next_weekday(date.today, 1)

    fecha_pedido = models.DateField(default=pedido)
    fecha_entrega = models.DateField(default=entrega)
    cantidad_pita_integral = models.IntegerField(default=0)
    cantidad_pita_blanco = models.IntegerField(default=0)
    cantidad_amasado_integral = models.IntegerField(default=0) 
    cantidad_amasado_blanco = models.IntegerField(default=0)
    nombre = models.CharField(max_length=120)
    email = models.EmailField()


