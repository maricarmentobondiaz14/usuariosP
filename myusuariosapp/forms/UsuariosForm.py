from django import forms
from django.forms import CheckboxInput

from myusuariosapp.models.Usuarios import Usuarios

class UsuariosForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = ('id_usuario','nombre','apellidop','apellidom','edad','email','telefono')
        widgets={
            'id_usuario':forms.TextInput(attrs={'class': 'input-form','placeholder':'Ingrese su clave de usuario',
                                                'required': 'true'}),
            'nombre': forms.TextInput(attrs={'class': 'input-form','placeholder':'Ingrese un nombre'}),
            'apellidop': forms.TextInput(attrs={'class':'input-form'}),
            'apellidom': forms.TextInput(attrs={'class': 'input-form'}),
            'edad': forms.NumberInput(attrs={'class': 'input-form'}),
            'email': forms.TextInput(attrs={'class': 'input-form'}),
            'telefono': forms.TextInput(attrs={'class': 'input-form'}),

        }

        def __init__(self, *args, **kwargs):
            super(UsuariosForm, self).__init__(*args, **kwargs)