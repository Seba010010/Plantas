#from django.db import models

# Create your models here.
#Modelo para la categoria 

#class Categoria(models.Model):
    #idCategoria = models.IntegerField(primary_key= True, verbose_name= 'id de categoria')
    #nombreCategoria = models.CharField(max_length=50, verbose_name = 'Nombre categoria')

    #def str(self):
        #return self.nombreCategoria

#Modelo para el vehiculo

#class producto(models.Model):
    #id_producto = models.CharField(max_length=6, primary_key= True, verbose_name='Id producto')
    #nombre =  models.CharField(max_length=20, verbose_name='Nombre producto')
    #categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    #def str(self):
        #return self.id_producto