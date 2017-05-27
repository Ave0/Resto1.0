from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurante(models.Model):
    nombre = models.CharField(max_length=50, default="")
    direccion = models.CharField(max_length=60)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    numero_mesas = models.IntegerField()
    tipo_comida = models.CharField(max_length=20)
    rango_precios = models.CharField(max_length=15)
    tiempo_espera = models.TimeField()
    telefono = models.CharField(max_length=50, null=True)
    ubicacion = models.CharField(max_length=200, null=True)
    tiempo_promedio_mesa = models.TimeField()
    descripcion = models.CharField(max_length=300, null=True)
    horario = models.CharField(max_length=200, null=True)
    usuario_resto = models.OneToOneField(User, on_delete=models.CASCADE)

class PreRegistro(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    numero_mesas = models.IntegerField()
    tipo_comida = models.CharField(max_length=20)
    rango_precios = models.CharField(max_length=15)
    tiempo_espera = models.TimeField()
    tiempo_promedio_mesa = models.TimeField()
    aceptado = models.BooleanField(default=False)
