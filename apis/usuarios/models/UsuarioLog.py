from django.db import models
from datetime import datetime
from .PerfilUsuario import PerfilUsuario

class UsuarioLog(models.Model):
    usuario = models.ForeignKey(
        PerfilUsuario, on_delete=models.CASCADE,
        related_name="logs_estado"
    )
    accion = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=datetime.now)
    motivo = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Log de Usuario"
        verbose_name_plural = "Logs de Usuarios"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.usuario.username} - {self.accion} ({self.fecha.strftime('%Y-%m-%d %H:%M')})"
