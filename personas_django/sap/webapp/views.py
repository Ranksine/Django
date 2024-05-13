from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona, Domicilio


# Create your views here.
def bienvenido(request):
    no_personas_var = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id', 'nombre')  # '-id' para ordenar de forma descendente
    return render(request, 'bienvenido.html', {'no_personas': no_personas_var, 'personas': personas})

def catalogoDomicilio(request):
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    return render(request, 'catalogoDomicilio.html', {'no_domicilios': no_domicilios, 'domicilios': domicilios})
