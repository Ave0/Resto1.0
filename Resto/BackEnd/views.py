from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate

# Create your views here.
def VistaEjemplo(request):
    contexto=[]
    return render(request, 'BackEnd/Base.html',contexto)

def VistaLogin(request):
	contexto = []
	return render(request, 'BackEnd/Login.html', contexto)

def BusquedaRestaurantes(request):
    return render("BusquedaRestaurantes.html")

def login_autentificar(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    autentificar = authenticate(username=email, password=password)
    if autentificar is not None:
        return HttpResponse("Si_Existe")
    return HttpResponse("No_Existe")
