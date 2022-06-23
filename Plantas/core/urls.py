from django.urls import path
from .views import Home, Contacto, Myaccount, Tienda, Registro, Nosotros

urlpatterns = [
    path('', Home, name= "Home"),
    path('Contacto', Contacto, name="Contacto"),
    path('Tienda', Tienda, name="Tienda"),
    path('Myaccount', Myaccount, name="Myaccount"),
    path('Registro', Registro, name="Registro"),
    path('Nosotros', Nosotros, name="Nosotros"),
]
