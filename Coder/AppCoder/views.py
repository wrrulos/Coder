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
    familiar1 = Familiares(nombre = 'Juan', apellido = 'Sanchez', parentesco = 'Padre', edad = 42, fechaNacimiento = '1980-06-05 03:15:34')
    familiar2 = Familiares(nombre = 'Pablo', apellido = 'Martinez', parentesco = 'Primo', edad = 18, fechaNacimiento = '2004-05-06 17:05:54')
    familiar3 = Familiares(nombre = 'Ayrton', apellido = 'Villamagna', parentesco = 'Hermano', edad = 20, fechaNacimiento = '2002-02-03 21:50:04')

    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    diccionario = {'familiares': [f'{familiar1.nombre} {familiar1.apellido} (Parentesco: {familiar1.parentesco}) ({familiar1.edad} años) (Fecha y Hora de Nacimiento: {familiar1.fechaNacimiento})', f'{familiar2.nombre} {familiar2.apellido} (Parentesco: {familiar2.parentesco}) ({familiar2.edad} años) (Fecha y Hora de Nacimiento: {familiar2.fechaNacimiento})', f'{familiar3.nombre} {familiar3.apellido} (Parentesco: {familiar3.parentesco}) ({familiar3.edad} años) (Fecha y Hora de Nacimiento: {familiar3.fechaNacimiento})']}

    plantilla = loader.get_template('familia.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)