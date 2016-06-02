from __future__ import unicode_literals

from django.db import models

class Proyecto(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1500)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre

class Estatus(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    estatus = models.ForeignKey(Estatus)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1500)
    fechainicio = models.DateTimeField(null=True)
    fechafin = models.DateTimeField(null=True)
    fecharegistro = models.DateTimeField(auto_now=True)
    fechalimite = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.nombre