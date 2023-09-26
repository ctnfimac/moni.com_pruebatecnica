from django.db import models
from .genero import Genero

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    dni = models.CharField(max_length=8, unique=True)
    genero = models.ForeignKey(Genero, on_delete=models.RESTRICT)

    fecha_de_alta = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.dni
