from multiprocessing import context
from tempfile import template
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime


def primervista (request):
    return HttpResponse("Gimnasio Squat")

def segundavista(request):
    return HttpResponse ("<h1> Gimnasio Squat </h1> <p> Hacelo bien, Hacelo Squat </p>")

def diahora_tercervista(request):
    fecha= datetime.now()
    return HttpResponse(f"<p> el tiempo ahora es {fecha} </p>")

def nombre_cuartavista(request, nombre):
    return HttpResponse(f"bienvenido/a {nombre}")
#ver el tema del nombre, no me aparece

def edad_usuario_quintavista(request, edad):
    anio_nac= 2022- int(edad)
    return HttpResponse("la edad no es un limite para lograr tus objetivos, puedes hacerlo")
#funciono pero a mipagina no le va a servir mucho la edad asi que no puse un f stream

def pag_inicio(request):

   archivo=open(r"C:\Users\PC\Desktop\PYTHON\TPfinal\tpfinal_axel\tpfinal_axel\templates\iniciopag.html", 'r')
   plantilla= template(archivo.read())

   archivo.close

   contexto= context()

   documento=plantilla.render(contexto)

   return HttpResponse(documento)
