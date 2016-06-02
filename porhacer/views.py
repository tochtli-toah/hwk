from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Al inicio de la lista de tareas")

def listaProyectos(request):
    return HttpResponse("Lista de proyectos")

def detalleProyecto(request,proyecto_id):
    return HttpResponse("Detalle de proyectos")

def editaProyecto(request,proyecto_id):
    return HttpResponse("Edita un proyectos")

def nuevaTarea(request):
    return HttpResponse("Nueva Tarea")

def editaTarea(request, tarea_id):
    return HttpResponse("Edita Tarea")
