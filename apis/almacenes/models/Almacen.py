from django.db import models
from django.core.validators import RegexValidator

class Almacen(models.Model):
    TIPO_ALMACEN_CHOICES = (
        ('archivos', 'Archivos'),
        ('material', 'material')
    )
    tipo_almacen = models.CharField(
        max_length=8, blank=False, null=False,
        validators=[
            RegexValidator(
                regex='^(archivos|material)',
                message='Tipo de almacén no válido.'
            )
        ]
    )
    ubicacion = models.TextField()

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Almacén'
        verbose_name_plural = 'Almacenes'

    def __str__(self):
        return f"{self.tipo_almacen} - {self.ubicacion}"
