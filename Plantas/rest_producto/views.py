
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import producto
from .serializers import ProductoSerializer
#from Plantas.rest_producto import serializers


#CREANDO SERVICIOS 
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_productos(request):

    "lista de productos"

    if request.method == 'GET':
        productos = producto.objects.all()
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#CREANDO SERVICIOS REST PUT, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_productos(request, id):

    "GET, UPDATE o DELETE de un producto"

    try:
        productos = producto.objects.get(id_producto = id)
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(productos)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(productos, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        productos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)