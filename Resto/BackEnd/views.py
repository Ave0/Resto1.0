from django.shortcuts import render

# Create your views here.
def VistaEjemplo(request):
    contexto=[]
    return render(request, 'BackEnd/Base.html',contexto)
