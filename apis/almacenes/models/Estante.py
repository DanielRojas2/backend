from django.db import models
from .Almacen import Almacen

class Estante(models.Model):
    nro_estante = models.PositiveSmallIntegerField()
    almacen = models.ForeignKey(
        Almacen,
        on_delete=models.CASCADE,
        related_name='estantes_almacen'
    )

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Estante'
        verbose_name_plural = 'Estantes'

    def __str__(self):
        return f"{self.nro_estante} - {self.almacen}"
