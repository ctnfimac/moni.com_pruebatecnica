from django.db import models 
from .usuario import Usuario

class Prestamo(models.Model):
    monto = models.BigIntegerField()
    aceptado = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.monto