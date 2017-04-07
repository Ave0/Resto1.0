from django.db import models
from django.forms.models import ModelForm
# Create your models here.


class Restaurante(models.Model):
    nombre=models.CharField(max_length=100)
    numero_mesas=models.IntegerField()
    direccion=models.CharField(max_length=100)
    horario=models.CharField(max_length=100)
    calificacion=models.IntegerField(default=10)
    def __unicode__(self):
        return self.nombre

class FormularioRestauranteForm(ModelForm):
    class Meta:
        model=Restaurante
        exclude=['calificacion']

class Platillo(models.Model):
    restaurante=models.ForeignKey(Restaurante)
    nombre_platillo=models.CharField(max_length=100)
    descripcion_platillo=models.CharField(max_length=100)
    precio=models.FloatField()
    def __unicode__(self):
        return self.nombre_platillo
