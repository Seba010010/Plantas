from django.urls import path
from .views import Home, Contacto, Form_mod_Contacto

urlpatterns = [
    path('', Home, name= "Home"),
]
from django.urls import path
from .views import Contacto

urlpatterns = [
    path('', Contacto, name="Contacto"),
    path('Contacto-form', Contacto, name= "Contacto")
]
from django.urls import path
from .views import Myaccount

urlpatterns = [
    path('', Myaccount, name="Myaccount"),
]

from django.urls import path
from .views import Tienda

urlpatterns = [
    path('', Tienda, name="Tienda"),
]

from django.urls import path
from .views import Registro

urlpatterns = [
    path('', Registro, name="Registro"),
]

from django.urls import path
from .views import Nosotros

urlpatterns = [
    path('', Nosotros, name="Nosotros"),
]