from django.urls import path
from rest_usuario import views
from rest_usuario.viewslogin import login
from rest_usuario.views import lista_usuarios, detalle_usuarios

urlpatterns = [
    path('lista_usuarios', lista_usuarios, name="lista_usuarios"),
    path('detalle_usuarios/<id>', detalle_usuarios, name= "detalle_usuarios"),
    path('lista_usuarios', views.lista_usuarios, name="lista_usuarios"),
    path('detalle_usuarios/<id>', views.detalle_usuarios, name= "detalle_usuarios"),
    path('login', login, name = "login"),
]