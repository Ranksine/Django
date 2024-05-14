from django.shortcuts import render

# Create your views here.
class Producto:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        super().__init__()

def home(request):
    vinilo = Producto("Vinilo de Black Album", 1999)
    
    lista = ["Iron man", "Capitán America", "Spiderman"]
    contexto = {"nombre": "Omars Aguilars"}
    return render(request, 'core/home.html', {'context': contexto, 'lista': lista, 'vinilo':vinilo})
