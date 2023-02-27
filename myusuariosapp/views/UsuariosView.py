#importar modelos
import json

from django.http import JsonResponse, HttpResponse
from django.http import  *
from myusuariosapp.models.Usuarios import Usuarios

#importar forms
from myusuariosapp.forms.UsuariosForm import UsuariosForm

# paquetes y librerias
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages



nombreUsuario=None




def ordenadorApellidop(lista):
    for i in range(0, len(lista) - 1):
        menor = i
        j = i + 1
        while j < len(lista):
            if lista[j]['apellidop'] < lista[menor]['apellidop']:
                menor = j
            j = j + 1
        aux = lista[i]['apellidop']
        aux1=lista[i]['apellidom']
        aux2=lista[i]['nombre']
        aux3=lista[i]['edad']
        aux4=lista[i]['email']
        aux5=lista[i]['telefono']
        aux7=lista[i]['id_usuario']



        lista[i]['apellidop'] = lista[menor]['apellidop']
        lista[i]['apellidom'] = lista[menor]['apellidom']
        lista[i]['nombre'] = lista[menor]['nombre']
        lista[i]['edad'] = lista[menor]['edad']
        lista[i]['email'] = lista[menor]['email']
        lista[i]['telefono'] = lista[menor]['telefono']
        lista[i]['id_usuario']=lista[menor]['id_usuario']

        lista[menor]['apellidop'] = aux
        lista[menor]['apellidom'] = aux1
        lista[menor]['nombre'] = aux2
        lista[menor]['edad'] = aux3
        lista[menor]['email'] = aux4
        lista[menor]['telefono'] = aux5
        lista[menor]['id_usuario']=aux7
        return lista


def ordenadorEdad(lista):
    for i in range(0, len(lista) - 1):
        menor = i
        j = i + 1
        while j < len(lista):
            if lista[j]['edad'] < lista[menor]['edad']:
                menor = j
            j = j + 1
        aux = lista[i]['apellidop']
        aux1=lista[i]['apellidom']
        aux2=lista[i]['nombre']
        aux3=lista[i]['edad']
        aux4=lista[i]['email']
        aux5=lista[i]['telefono']
        aux7=lista[i]['id_usuario']



        lista[i]['apellidop'] = lista[menor]['apellidop']
        lista[i]['apellidom'] = lista[menor]['apellidom']
        lista[i]['nombre'] = lista[menor]['nombre']
        lista[i]['edad'] = lista[menor]['edad']
        lista[i]['email'] = lista[menor]['email']
        lista[i]['telefono'] = lista[menor]['telefono']
        lista[i]['id_usuario']=lista[menor]['id_usuario']

        lista[menor]['apellidop'] = aux
        lista[menor]['apellidom'] = aux1
        lista[menor]['nombre'] = aux2
        lista[menor]['edad'] = aux3
        lista[menor]['email'] = aux4
        lista[menor]['telefono'] = aux5
        lista[menor]['id_usuario']=aux7

    return lista



def vw_ordenar_apellidop(request):

    vwUsuarios = Usuarios.objects.all()
    lista_usuarios = []
    for usu in vwUsuarios:
        data_usuario = {}
        data_usuario['id_usuario'] = usu.id_usuario
        data_usuario['nombre'] = usu.nombre
        data_usuario['apellidop'] = usu.apellidop
        print(data_usuario['apellidop'])
        data_usuario['apellidom'] = usu.apellidom
        data_usuario['edad'] = usu.edad
        data_usuario['email'] = usu.email
        data_usuario['telefono'] = usu.telefono
        lista_usuarios.append(data_usuario)

    lista2 = ordenadorApellidop(lista_usuarios)
    data = json.dumps(lista2)
    decoded_data = json.loads(data)

    return render(request, 'myusuariosapp/usuarios_list_ordenarApellido.html',
                  {'data_serie': decoded_data}
                           )

def vw_ordenar_edad(request):
    vwUsuarios = Usuarios.objects.all()
    lista_usuarios = []
    for usu in vwUsuarios:
        data_usuario = {}
        data_usuario['id_usuario'] = usu.id_usuario
        data_usuario['nombre'] = usu.nombre
        data_usuario['apellidop'] = usu.apellidop
        print(data_usuario['apellidop'])
        data_usuario['apellidom'] = usu.apellidom
        data_usuario['edad'] = usu.edad
        data_usuario['email'] = usu.email
        data_usuario['telefono'] = usu.telefono
        lista_usuarios.append(data_usuario)

    lista2 = ordenadorEdad(lista_usuarios)
    data = json.dumps(lista2)
    decoded_data = json.loads(data)

    return render(request, 'myusuariosapp/usuarios_list_ordenarEdad.html',
                  {'data_serie': decoded_data}
                  )


def vw_usuarios_list(request):
  vwUsuarios= Usuarios.objects.all()
  return render(request, 'myusuariosapp/usuarios_list.html', {'vwUsuarios': vwUsuarios
                                                              })

#Editar usuarios
def vw_usuarios_edit(request,pk):
    messages.info(request, 'Editar Usuario')
    usuario_vw = get_object_or_404(Usuarios, pk=pk)
    if request.method == "POST":
        form = UsuariosForm(request.POST, instance=usuario_vw)
        print(form)
        if form.is_valid():
            form.save()
            print(usuario_vw)
            print("Guardar")
            messages.info(request, 'El usuario se edito correctamente')

            return redirect('url_usuarios_list')
    else:
        form = UsuariosForm(instance=usuario_vw)
    return render(request, 'myusuariosapp/usuarios_edit.html', {'form': form, 'usuario_vw': usuario_vw})




#Agregar usuarios
def vw_usuarios_new(request):
    form = UsuariosForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'El usuario se agregó correctamente')
        return redirect('url_usuarios_list')
    else:

        form = UsuariosForm()
        return render(request, 'myusuariosapp/usuarios_edit.html', {'form': form } )


#Eliminar usuarios
def vw_usuarios_delete(request,pk):
    try:
        usuario = Usuarios.objects.filter(id_usuario=pk)
        usuario.delete()
        messages.success(request, 'El usuario se eliminó Correctamente')
        return redirect('url_usuarios_list')
    except:
        print("Error...")
        messages.error(request, 'El usuario que quiere eliminar tiene dependencias asociadas')
        return redirect('url_usuarios_list')















