"""
(ForeignKey - Uno a Muchos)
class Persona(models.Model):
    atributos...

class Mascota(models.Model):
    persona = models.ForeignKey(Persona, null= true, blank=True, on_delete=models.CASCADE)
    atributos...

(OneToOneField - Uno a uno)
class Persona(models.Model):
    atributos...

class Mascota(models.Model):
    persona = models.OneToOneField(Persona, null= true, blank=True, on_delete=models.CASCADE)
    atributos...

(ManyToManyField - Muchos a Muchos)
class Vacuna(models.Model):
    atributos...

class Mascota(models.Model):
    vacuna = models.ManyToManyField(Vacuna)
    atributos...

"""

from django.db import models
from datetime import date
from configurador.models import Comuna, Provincia, Region

# Create your models here.
class Pan(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=70)
    descripcion = models.TextField(max_length=100)
    valor = models.IntegerField()


class Persona(models.Model):    
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido_paterno = models.CharField(max_length=70)
    apellido_materno = models.CharField(max_length=70)
    fecha_nacimiento = models.DateField()
    telefono_movil = models.CharField(max_length=9)
    email = models.EmailField()

    def __str__(self):
        self.nombre_completo = ''.join([self.nombre, ' ', self.apellido_paterno, ' ', self.apellido_materno])
        return self.nombre_completo

class Direccion(models.Model):    
    NINGUNO = '0'
    CASA = '1'
    DEPARTAMENTO = '2'
    OTRO = '3'

    TIPO_INMUEBLE = (
        (NINGUNO, 'Ninguno'),
        (CASA, 'Casa'),
        (DEPARTAMENTO, 'Departamento'),
        (OTRO, 'Otro'),
    )

    inmueble = models.CharField(max_length=2, choices=TIPO_INMUEBLE, default=NINGUNO)
    calle = models.CharField(max_length=80)
    numero = models.IntegerField()
    referencia = models.TextField(max_length=150)
    comuna = models.ForeignKey(Comuna, db_column="comuna", null=True, blank=True)
    provincia = models.ForeignKey(Provincia, db_column="provincia", null=True, blank=True)
    region = models.ForeignKey(Region, db_column="region", null=True, blank=True)
    persona = models.ForeignKey(Persona, db_column="rut", null=True, blank=True, on_delete=models.CASCADE)

class Detalle(models.Model):
    fecha_pedido = models.DateField(default=date.today)
    fecha_entrega = models.DateField()
    cantidad_pita_integral = models.IntegerField(default=0)
    cantidad_pita_blanco = models.IntegerField(default=0)
    cantidad_amasado_integral = models.IntegerField(default=0) 
    cantidad_amasado_blanco = models.IntegerField(default=0)
    cantidad_panes = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    persona = models.ForeignKey(Persona, db_column="rut", null=True, blank=True, on_delete=models.CASCADE)
