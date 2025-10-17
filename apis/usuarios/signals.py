from datetime import date
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models.PerfilUsuario import PerfilUsuario

@receiver(pre_save, sender=PerfilUsuario)
def asegurar_activo_en_creacion_y_reglas(sender, instance, **kwargs):
    hoy = date.today()
    siguiente_anio = hoy.year + 1

    if getattr(instance, "_state", None) and getattr(instance._state, "adding", False):
        instance.usuario_activo = True
        if not instance.baja:
            instance.baja = date(siguiente_anio, 1, 10)
        return

    if instance.usuario_activo and not instance.baja:
        instance.baja = date(siguiente_anio, 1, 10)

    if instance.baja and instance.baja <= hoy:
        instance.usuario_activo = False
