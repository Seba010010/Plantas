from django.urls import path
from .views import Home, Contacto, Myaccount, Tienda, Registro, Nosotros

urlpatterns = [
    path('', Home, name= "Home"),
    path('', Contacto, name="Contacto"),
    path('', Myaccount, name="Myaccount"),
    path('', Tienda, name="Tienda"),
    path('', Registro, name="Registro"),
    path('', Nosotros, name="Nosotros"),
]
