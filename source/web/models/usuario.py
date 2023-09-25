from django.db import models
from .genero import Genero

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    dni = models.CharField(max_length=8)
    genero = models.ForeignKey(Genero, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.dni
