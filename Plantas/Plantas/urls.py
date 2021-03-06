"""Plantas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from core import views
from django.urls import path, include
from django.contrib import admin
# import settings and static first
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets


#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('core.urls')),
#]

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.Home, name="Home"),
    path('Tienda/', views.Tienda, name="Tienda"),
    path('Nosotros/', views.Nosotros, name="Nosotros"),
    path('Myaccount/', views.Myaccount, name="Myaccount"),
    path('contacto/', views.Contacto, name="Contacto"),
    path('Registro/', views.Registro, name="Registro"),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/', include('rest_producto.urls')),
    path('api/', include('rest_usuario.urls')),
]

# add this lines
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)