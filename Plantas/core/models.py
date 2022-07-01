from contextlib import nullcontext
from logging import root
from nturl2path import url2pathname
from django.db import models

# Create your models here.

#Modelo para la categoria 

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key= True, verbose_name= 'id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name = 'Nombre categoria')

    def str(self):
        return self.nombreCategoria

#Modelo para los porductos

class producto(models.Model):
     
    imagen = models.ImageField(blank=True, upload_to='producto')
    id_producto = models.IntegerField(primary_key= True, verbose_name='Id producto')
    nombre =  models.CharField(max_length=20, verbose_name='Nombre producto')
    precio = models.PositiveIntegerField(null=True, blank=True, verbose_name='Precio')
    nombre_categoria = models.CharField( null= True, max_length=20, verbose_name='Categoria')
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def str(self):
        return self.id_producto

#modelo para form contacto

class ContactoForm(models.Model):

    nombre= models.CharField(max_length=30, primary_key=True, verbose_name='Nombre')
    email= models.CharField(max_length=20, verbose_name='Email')
    mensaje= models.CharField(max_length=20, verbose_name='Mensaje')

    def str(self):
        return self.mensaje