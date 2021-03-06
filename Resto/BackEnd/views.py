from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from models import *
from django.db.models import Q, Count

# Create your views here.
def VistaEjemplo(request):
    contexto={}
    return render(request, 'BackEnd/busquedarestaurantes.html',contexto)

def VistaLogin(request):
	contexto = {}
	return render(request, 'BackEnd/Login.html', contexto)

def BusquedaRestaurantes(request):
    context = {}
    listado_restaurantes = Restaurante.objects.all()


    resultado_busqueda = ""
    if request.GET:
        texto = request.GET.get('texto')
        if texto:
            try:
                resultado_busqueda = Restaurante.objects.filter(
                    Q(nombre__contains=texto) | Q(direccion__contains=texto) | Q(tipo_comida__contains=texto))
                listado_restaurantes = resultado_busqueda
            except Restaurante.DoesNotExist:
                listado_restaurantes = None

    context = {
        'listado_restaurantes': listado_restaurantes,
    }
    return render(request, "BackEnd/busquedarestaurantes.html", context)


def login_autentificar(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    autentificar = authenticate(username=email, password=password)
    if autentificar is not None:
        return HttpResponse("Si_Existe")
    return HttpResponse("No_Existe")


def mostarRestaurantes(request):
    latitudes=[]
    longitudes=[]
    diccionario={}
    restaurantes = models.Restaurante.objects.all().values("latitud" , "longitud")

    for data_latitud in restaurantes:
        latitudes.append(data_latitud.latitud)
        latitudes.append('1.023')
    for data_longitud in restaurantes:
        longitudes.append(data_longitud.longitud)
        longitudes.append('2.54')

    diccionario["latitudes"] = latitudes
    diccionario["longitudes"] = longitudes
    return JsonResponse(diccionario)

def registrar_restaurante(request):
    nombre = request.POST.get("nombre")
    email = request.POST.get("email")
    password = request.POST.get("password")
    direccion = request.POST.get("direccion")
    latitud = request.POST.get("latitud")
    longitud = request.POST.get("longitud")
    numero_mesas = request.POST.get("numero_mesas")
    tipo_comida = request.POST.get("tipo_comida")
    rango_precios = request.POST.get("rango_precios")
    tiempo_espera = request.POST.get("tiempo_espera")
    tiempo_promedio_mesa = request.POST.get("tiempo_mesa")
    registro = PreRegistro(nombre=nombre, email=email, password=password, direccion=direccion,
        latitud=latitud, longitud=longitud, numero_mesas=numero_mesas, tipo_comida=tipo_comida,
        rango_precios=rango_precios, tiempo_espera=tiempo_espera, tiempo_promedio_mesa=tiempo_promedio_mesa)
    registro.save()
    return HttpResponse("REgistro")
