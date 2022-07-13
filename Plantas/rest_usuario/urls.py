from django.urls import path
from rest_usuario.views import lista_usuarios

urlpatterns = [
    path('lista_usuarios', lista_usuarios, name="lista_usuarios"),
    #path('detalle_productos/<id>', detalle_productos, name= "detalle_productos"),
]