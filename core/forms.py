from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Contacto, producto

#creación de clase

class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields =['nombreContacto','emailContacto','mensajeContacto']

#class producto(ModelForm):
    #class Meta: 
        #model= producto
        #field = ['id_producto''nombre''categoria']

        