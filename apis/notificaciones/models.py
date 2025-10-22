from django.db import models
from django.utils import timezone
from ..usuarios.models.PerfilUsuario import PerfilUsuario

class Notificacion(models.Model):
    usuario = models.ForeignKey(
        PerfilUsuario,
        on_delete=models.CASCADE,
        related_name='notificaciones',
        blank=False, null=False
    )
    titulo = models.CharField(max_length=100, blank=False, null=False)
    mensaje = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    leido = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.usuario.username} - {self.titulo}"
