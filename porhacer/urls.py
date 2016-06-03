"""hwk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^proyectos/$', views.listaProyectos, name='listaproy'),
    url(r'^proyecto/$', views.nuevoProyecto, name='nuevoproyecto'),
    url(r'^proyecto/(?P<proyecto_id>[0-9]+)/$', views.detalleProyecto, name='detalleproy'),
    url(r'^proyecto/des/(?P<proyecto_id>[0-9]+)/$', views.desactivaProyecto, name='desactivaproy'),
    url(r'^proyecto/activ/(?P<proyecto_id>[0-9]+)/$', views.activaProyecto, name='activaproy'),
    url(r'^tarea/$', views.nuevaTarea, name='nuevatarea'),
    url(r'^tarea/inicia/(?P<tarea_id>[0-9]+)/$', views.iniciaTarea, name='iniciat'),
    url(r'^tarea/termina/(?P<tarea_id>[0-9]+)/$', views.terminaTarea, name='terminat'),
    url(r'^tarea/cancela/(?P<tarea_id>[0-9]+)/$', views.cancelaTarea, name='cancelat'),
    url(r'^contactos/$', views.contactos, name='contactos'),
]
