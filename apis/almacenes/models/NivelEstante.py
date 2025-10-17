from django.db import models
from .Estante import Estante
from .Nivel import Nivel

class NivelEstante(models.Model):
    estante = models.ForeignKey(Estante, on_delete=models.CASCADE, related_name='estante_nivel')
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name='nivel_estante')

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Nivel de Estante'
        verbose_name_plural = 'Nivel de Estante'
        constraints = [
            models.UniqueConstraint(
                fields=['estante', 'nivel'],
                name='unique_nivel_estante'
            )
        ]

    def __str__(self):
        return f"{self.nivel} - {self.estante}"
