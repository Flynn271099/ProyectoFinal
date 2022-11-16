from django.db import models

# Create your models here.
class Jefe(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    sueldo = models.IntegerField()
    email = models.EmailField('', null=True)

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    sueldo = models.IntegerField()
    email = models.EmailField('', null=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField('', null=True)