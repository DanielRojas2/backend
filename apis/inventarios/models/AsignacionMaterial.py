from django.db import models
from ...material.models.Material import Material
from ...almacenes.models.NivelEstante import NivelEstante

class AsignacionMaterial(models.Model):
    cantidad_asignada = models.PositiveSmallIntegerField(
        default=1, blank=False, null=False
    )
    cantidad_existente = models.PositiveSmallIntegerField(
        blank=True, null=True
    )
    fecha_asignacion = models.DateField(auto_now_add=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    nivel_estante = models.ForeignKey(NivelEstante, on_delete=models.CASCADE)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Asignacion de Material'
        verbose_name_plural = 'Asignacion de Materiales'
    
    def __str__(self):
        return f"{self.material} - {self.cantidad_asignada}, {self.nivel_estante}"
