from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .Cargo import Cargo
from ..managers.PerfilUsuarioManager import PerfilUsuarioManager

class PerfilUsuario(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    nombre = models.CharField(max_length=25, blank=False, null=False)
    apellido_paterno = models.CharField(
        max_length=25, blank=False, null=False
    )
    apellido_materno = models.CharField(
        max_length=25, blank=True, null=True
    )
    usuario_activo = models.BooleanField(blank=False, null=False, default=True)
    usuario_admin = models.BooleanField(default=False)
    alta = models.DateField(auto_now_add=True)
    baja = models.DateField(blank=True, null=True)
    cargo = models.ForeignKey(
        Cargo, on_delete=models.CASCADE, related_name='perfiles_usuarios',
        blank=True, null=True
    )
    
    objects = PerfilUsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido_paterno']

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"
        ordering = ['nombre', 'apellido_paterno']
        constraints = [
            models.UniqueConstraint(
                fields=['nombre', 'apellido_paterno', 'apellido_materno'],
                name='unique_nombre_apellidos'
            )
        ]
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno or ''}".strip()
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_active(self):
        return self.usuario_activo

    @property
    def is_staff(self):
        return self.usuario_activo

    @property
    def is_superuser(self):
        return self.usuario_admin

    def dar_baja_manual(self, motivo=None, fecha_baja=None):
        self.baja = fecha_baja or date.today()
        self.usuario_activo = False
        self.save()

        return True
