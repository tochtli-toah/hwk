from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Estatus, Proyecto, Tarea
from .forms import NuevaTareaForm, NuevoProyectoForm

def index(request):
    listatareas = Tarea.objects.all()
    context = {'listatareas': listatareas,}
    return render (request, 'tareas/listatareas.html', context)

def listaProyectos(request, mensaje=None):
    listaproyectos = Proyecto.objects.all()
    context = {'listaproyectos': listaproyectos,}
    return render (request, 'proyectos/listaproyectos.html', context)

def detalleProyecto(request,proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    if proyecto:
        return render (request, 'proyectos/detalleproyecto.html', {
                'proyecto': proyecto,
            })
    else:
        return redirect('listaproy', mensaje = 'El proyecto solicitado no existe')

def activaProyecto(request,proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    if proyecto or proyecto.activo == False :
        proyecto.activo = True
        proyecto.save()
    return redirect('listaproy')
    
def desactivaProyecto(request,proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    if proyecto or proyecto.activo == True :
        proyecto.activo = False
        proyecto.save()
    return redirect('listaproy')
    
def nuevoProyecto(request):
    if request.method == 'POST':
        form = NuevoProyectoForm(request.POST)
        if form.is_valid():
            pp = Proyecto()
            pp.nombre = request.POST.get('nombre')
            pp.descripcion = request.POST.get('descripcion')
            pp.activo = request.POST.get('activo',False)
            pp.save()
            return redirect('listaproy')
    else:
        form = NuevoProyectoForm()
    return render(request, 'proyectos/formproyecto.html', {'form': form})

def nuevaTarea(request):
    if request.method == 'POST':
        form = NuevaTareaForm(request.POST)
        if form.is_valid():
            tt = Tarea()
            tt.proyecto = Proyecto.objects.get(pk=request.POST.get('proyecto'))
            tt.estatus = Estatus.objects.get(pk=1)
            tt.nombre = request.POST.get('nombre')
            tt.descripcion = request.POST.get('descripcion')
            tt.save()
            return redirect('index')
    else:
        form = NuevaTareaForm()
    return render(request, 'tareas/formtarea.html', {'form': form})

def iniciaTarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    if tarea_id:
        estatus = Estatus.objects.get(pk=2)
        tarea.status = estatus
        tarea.fechainicio = timezone.now()
        tarea.save()
    return redirect('index')
    
def terminaTarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    if tarea_id:
        estatus = Estatus.objects.get(pk=3)
        tarea.status = estatus
        tarea.fechainicio = timezone.now()
        tarea.save()
    return redirect('index')
    
def cancelaTarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    if tarea_id:
        estatus = Estatus.objects.get(pk=4)
        tarea.status = estatus
        tarea.fechainicio = timezone.now()
        tarea.save()
    return redirect('index')

def contactos(request):
    return render (request, 'contactos/contactos.html')