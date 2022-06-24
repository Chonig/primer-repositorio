from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime 




def saludar (request):
    fecha_hora = datetime.now()
    return HttpResponse (f" Hola Cristian, la hora es : {fecha_hora}")
# Create your views here.


def saludar_a(request, pipi):
    return HttpResponse (f" Hola como estas? {pipi.upper()}")



def nombre (request):
    return HttpResponse ( " Cristian Hönig ")


def suma ( request):
    return HttpResponse ( 1 + 1 )

