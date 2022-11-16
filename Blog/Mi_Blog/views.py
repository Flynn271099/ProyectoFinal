from django.shortcuts import render
from Mi_Blog.models import *
from Mi_Blog.forms import *

# Create your views here.
def index(request):
    
    return render(request, 'Mi_Blog/index.html')

def C_Empleado(request):
        
    formulario = AniadirEmpleado()
    
    if request.method == "POST":
        
        formulario = AniadirEmpleado(request.POST)
        
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            empleado = Empleado(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], sueldo=formulario_limpio['sueldo'], email=formulario_limpio['email'])
            
            empleado.save()

            return render(request, 'Mi_Blog/index.html')
    
    else:
        formulario = AniadirEmpleado()
    
    return render(request, 'Mi_Blog/empleado.html', {'formulario': AniadirEmpleado})

def C_Jefe(request):
        
    formulario = AniadirJefe()
    
    if request.method == "POST":
        
        formulario = AniadirJefe(request.POST)
        
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            jefe = Jefe(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], sueldo=formulario_limpio['sueldo'], email=formulario_limpio['email'])
            
            jefe.save()

            return render(request, 'Mi_Blog/index.html')
    
    else:
        formulario = AniadirJefe()
    
    return render(request, 'Mi_Blog/jefe.html', {'formulario': AniadirJefe})

def C_Cliente(request):
        
    formulario = AniadirCliente()
    
    if request.method == "POST":
        
        formulario = AniadirCliente(request.POST)
        
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            cliente = Cliente(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'])
            
            cliente.save()

            return render(request, 'Mi_Blog/index.html')
    
    else:
        formulario = AniadirCliente()
    
    return render(request, 'Mi_Blog/cliente.html', {'formulario': AniadirCliente})


def buscar_cliente(request):
    
    if request.GET.get('email', False):
        
        email = request.GET['email']
        clientes = Cliente.objects.filter(email__icontains=email)
        
        return render(request, 'Mi_Blog/buscar_cliente.html', {'clientes': clientes})
    else:
        
        respuesta = 'No hay datos.'
    
    return render(request, 'Mi_Blog/buscar_cliente.html', {'respuesta': respuesta})