from django.db import models

class Presentacion(models.Model):
    presentacion = models.CharField(
        max_length=50, unique=True, blank=False, null=False
    )

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Presentación'
        verbose_name_plural = 'Presentación'

    def __str__(self):
        return self.presentacion
