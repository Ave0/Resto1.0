from django.shortcuts import render
from BackEnd.models import Restaurante

# Create your views here.
def detalles(request):
    return render(request, "FrontEnd/detalles.html")

def HomeLanding(request):
    listado_restaurantes = Restaurante.objects.all()
    context = {
        'listado_restaurantes': listado_restaurantes,
    }
    return render(request, "FrontEnd/index.html", context)
