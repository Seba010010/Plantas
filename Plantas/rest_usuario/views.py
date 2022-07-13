from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import RegistroForm
from .serializers import RegistroFormSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#CREANDO SERVICIOS 
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated))
def lista_usuarios(request):

    "lista de usuarios"

    if request.method == 'GET':
        registro = RegistroForm.objects.all()
        serializer = RegistroFormSerializer(registro, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistroFormSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

#CREANDO SERVICIOS REST PUT, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated))
def detalle_usuarios(request, id):

    "GET, UPDATE o DELETE de un USUARIO"

    try:
        registro = RegistroForm.objects.get(correo = id)
    except RegistroForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RegistroFormSerializer(registro)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegistroFormSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
