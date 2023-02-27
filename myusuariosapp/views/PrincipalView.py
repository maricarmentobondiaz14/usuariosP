from myusuariosapp.models.Usuarios import Usuarios
from django.shortcuts import render, redirect

from django.http.response import HttpResponse
from django.contrib import messages


def vw_inicio(request):
    return redirect('url_usuarios_list')
