from django.db import models


class Genero(models.Model):
    tipo = models.CharField(max_length=20)

    fecha_de_alta = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.tipo