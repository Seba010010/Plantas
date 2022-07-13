from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Contacto, producto, RegistroForm

#creación de clase

class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields =['nombreContacto','emailContacto','mensajeContacto']

class producto(ModelForm):
    class Meta: 
        model= producto
        field = ['id_producto''nombre''categoria']



class RegistroForm(ModelForm):

    class Meta:
        model = RegistroForm
        fields =['nombres','apellidos','correo', 'contrasena']
        