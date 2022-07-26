from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from miapp.models import Estudiante
# Create your views here.
layout = """"""
def integrantes(request):
    integrantes = ['Jose Andres Vera Rodriguez','Paulino Alfonso Conteras Gómez','Piero Carlos Vidal Hinostroza Bellido']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Bienvenidos',
        'mensaje':'Proyecto para la Unidad de Competencia 04 (UC04)'
    })

def crear_estudiante(request):
 estudiante = Estudiante(
 codigo = "1822138559",
 dni = "71255610",
 nombre = "Jaime",
 apepat = "Duarte",
 apemat = "Uribe",
 direccion = "Magdanela Jr. nº 1414",
 telefono = "9123667699",
 estado = "A"
 )
 estudiante.save()
 return HttpResponse (f"<h1>Estudiante registrado:</h1> "+
 f"<br> <b>Código:</b> {estudiante.codigo} <br> <b>DNI:</b> {estudiante.dni} <br> <b>Nombre:</b> {estudiante.nombre} <br> "+
 f"<b>Apellido paterno:</b> {estudiante.apepat} <br> <b>Apellido materno:</b> {estudiante.apemat} <br><b>Dirección:</b> "+
 f" {estudiante.direccion} <br> <b>Telefono:</b> {estudiante.telefono} <br> <b>Estado:</b> {estudiante.estado}")
