from django.shortcuts import render

# Create your views here.
def detalles(request):
    return render(request, "FrontEnd/detalles.html")
