from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import producto
from .serializers import ProductoSerializer
#from Plantas.rest_producto import serializers

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
