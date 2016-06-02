from django.contrib import admin
from .models import Proyecto, Estatus, Tarea

admin.site.register(Estatus)
admin.site.register(Proyecto)
admin.site.register(Tarea)