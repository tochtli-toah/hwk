# -*- coding: utf8 -*-
from django import forms
from .models import Proyecto, Estatus

class NuevaTareaForm(forms.Form):
    proyectos = Proyecto.objects.filter(activo=True)
    proyectosch = [(p.id,p.nombre) for p in proyectos]
    proyecto = forms.ChoiceField(choices=proyectosch,required=True, label='Proyecto')
    nombre = forms.CharField(label='Nombre de la tarea',required=True ,max_length=200)
    descripcion = forms.CharField(label='Descripción',required=True ,max_length=1500, widget=forms.Textarea)


class NuevoProyectoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del proyecto',required=True ,max_length=200)
    descripcion = forms.CharField(label='Descripción',required=True ,max_length=1500, widget=forms.Textarea)
    activo = forms.BooleanField(label='Proyecto activo',required=False)