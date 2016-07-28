from django.db import models
from django.utils import timezone

import datetime

def calcula_siguente_martes():
    dia = datetime.date.today()
    while dia.weekday() != 1:           
        dia += datetime.timedelta(1)
    return dia

# Create your models here.
class Pan(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=70)
    descripcion = models.TextField(max_length=100)
    valor = models.IntegerField()

    def __str__(self):
        return '[%s]' % (self.nombre)
    
class Detalle(models.Model):
    fecha_pedido = models.DateField(default=timezone.now)
    fecha_entrega = models.DateField(default=calcula_siguente_martes())
    cantidad_pita_integral = models.IntegerField(default=0)
    cantidad_pita_blanco = models.IntegerField(default=0)
    cantidad_amasado_integral = models.IntegerField(default=0) 
    cantidad_amasado_blanco = models.IntegerField(default=0)
    nombre = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return '[%s] %s' % ('Pedido', self.nombre)

