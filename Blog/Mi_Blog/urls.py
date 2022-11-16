from django.urls import path
from Mi_Blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('C_Empleado/', views.C_Empleado, name='Nuevo Empleado'),
    path('C_jefe/', views.C_Jefe, name='Nuevo Jefe'),
    path('C_Cliente/', views.C_Cliente, name='Nuevo Cliente'),
    path('buscar_cliente/', views.buscar_cliente, name='Buscar Cliente'),
]