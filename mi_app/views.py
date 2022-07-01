from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime 
from mi_app.models import Curso



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

def saludo_personalizado( request ):
    context = {}
    return render ( request,"mi_app/index.html", context)


def listar( request ):
    context = {}
    context["cursos"]= Curso.objects.all()
    return render ( request, "mi_app/index.html", context )