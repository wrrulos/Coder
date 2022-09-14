from contextvars import Context
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from AppCoder.models import Familiares

# Create your views here.


def guardarDatos(self):
    """
    Guarda los datos de los familiares en la base de datos.
    """
    familiar1 = Familiares(nombre = 'Juan', apellido = 'Sanchez', parentesco = 'Padre', edad = 42, fechaNacimiento = '1980-06-05')
    familiar2 = Familiares(nombre = 'Pablo', apellido = 'Hermano', parentesco = 'Padre', edad = 18, fechaNacimiento = '2004-05-06')
    familiar3 = Familiares(nombre = 'Ayrton', apellido = 'Primo', parentesco = 'Padre', edad = 20, fechaNacimiento = '2002-02-03')

    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    #diccionario = {'familiares':[familiar1.nombre, familiar2.nombre, familiar3.nombre]}

    plantilla = loader.get_template('familia.html')
    #miContexto = Context(diccionario)
    documento = plantilla.render()

    return HttpResponse(documento)

