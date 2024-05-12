from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    mensajes = {'msg1':'Valor mensaje 1', 'msg2':'Valor mensaje 2'}  # Tambien se puede pasar directamente el diccionario en lugar de la variable mensajes
    return render(request, 'bienvenido.html', mensajes)  # return HttpResponse('Hola mundo desde Django')


