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

class Region(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Provincia(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=100)
	region = models.ForeignKey(Region, db_column="region", null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Comuna(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=100)
	provincia = models.ForeignKey(Provincia, db_column="provincia", null=True, blank=True, on_delete=models.CASCADE)
	region = models.ForeignKey(Region, db_column="region", null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Pan(models.Model):
	tipo = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=200)
