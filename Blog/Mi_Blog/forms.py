from django import forms

class AniadirEmpleado(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    sueldo = forms.IntegerField()
    email = forms.EmailField()
    
class AniadirJefe(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    sueldo = forms.IntegerField()
    email = forms.EmailField()

class AniadirCliente(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()