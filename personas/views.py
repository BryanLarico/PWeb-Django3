from django.shortcuts import render
from .models import Persona

# Create your views here.
def personaTestView(request, *args, **kwargs):
    obj = Persona.objects.get(id = 1)
    context = {
        'nombre': obj.nombre,
        'apellidos': obj.apellidos,
        'edad': obj.edad,
        }
    return render(request, 'personas/test.html', context)