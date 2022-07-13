from rest_framework import serializers
from core.models import RegistroForm

class RegistroFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroForm
        fields= ['nombres', 'apellidos', 'correo', 'contrasena']