from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from core.models import producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields= ['imagen', 'id_producto', 'nombre', 'precio', 'nombre_categoria', 'categoria']