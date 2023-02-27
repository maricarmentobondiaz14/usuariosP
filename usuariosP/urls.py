"""usuariosP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myusuariosapp.views.UsuariosView import *
from myusuariosapp.views.PrincipalView import *


urlpatterns = [
    path('usuarios/new', vw_usuarios_new, name='url_usuarios_new'),
    path('usuarios/', vw_usuarios_list, name='url_usuarios_list'),
    path('usuarios/<pk>/editar', vw_usuarios_edit, name='url_usuarios_edit'),
    path('usuarios/<pk>/eliminar', vw_usuarios_delete, name='url_usuarios_delete'),
    path('usuarios/ordenarApellido',vw_ordenar_apellidop,name='url_usuarios_ordenarApellido'),
    path('usuarios/ordenarEdad', vw_ordenar_edad, name='url_usuarios_ordenarEdad'),

    #path('', include('pedidosapp.urls')),
    path('', vw_inicio, name='url_inicio')
]
