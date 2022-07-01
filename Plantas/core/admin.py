from django.contrib import admin
from .models import Categoria, producto, ContactoForm

# Register your models here.

admin.site.register(Categoria)
admin.site.register(producto)
admin.site.register(ContactoForm)