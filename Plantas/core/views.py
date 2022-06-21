from django.shortcuts import render
from .models import producto

# Create your views here.

def Home(request):
    return render(request, 'core/Home.html')
    
def Contacto(request):
    return render(request, 'core/Contacto.html')

def Myaccount(request):
    return render(request, 'core/Myaccount.html')

def Nosotros(request):
    return render(request, 'core/Nosotros.html')

def Tienda(request):
    return render(request, 'core/Tienda.html')

def Registro(request):
    return render(request, 'core/Registro.html')


def ContactoForm(request):
    return render(request,'core/ContactoForm.html')



def ContactoForm(request):
    datos ={
        'form':ContactoForm
    }
    if request.method=='post':
        formulario = ContactoForm(data= request.post, instance= Contacto)

        
        if formulario.is_valid:
            formulario.save
            datos['MENSAJE']="Datos guardados exitosamente"

    return render(request, 'core/ContactoForm.html', datos)

def Form_mod_Contacto(request, id):
    Contacto = ContactoForm.objects.get(nombre = id)
    datos = {
        'form': ContactoForm(instance = Contacto)
    }

def tienda(request):
    productos = producto.objects.all()

    datos = {
        'productos': productos
    }

    return render(request, 'core/Tienda.html', datos)
