from django.db import models 
from .usuario import Usuario

class Prestamo(models.Model):
    monto = models.BigIntegerField(default=0)
    aceptado = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)

    fecha_de_alta = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return str(self.monto)