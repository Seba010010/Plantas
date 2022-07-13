from django.contrib import admin
from .models import Categoria, producto, ContactoForm, RegistroForm

# Register your models here.

admin.site.register(Categoria)
admin.site.register(producto)
admin.site.register(ContactoForm)
admin.site.register(RegistroForm)