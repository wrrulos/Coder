from django.db import models

# Create your models here.

class Familiares(models.Model):
    """
    DB Familiares
    """
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    parentesco = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaNacimiento = models.DateTimeField()