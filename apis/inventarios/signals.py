from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from .models import AsignacionMaterial

@receiver([post_save, post_delete], sender=AsignacionMaterial)
def actualizar_inventario(sender, instance, **kwargs):
    """
    Recalcula automáticamente:
    1. cantidad_existente de todas las asignaciones del mismo material
       (sumando sus cantidad_asignada).
    2. cantidad_existente del Material principal.
    """

    material = instance.material

    total_asignada = (
        AsignacionMaterial.objects
        .filter(material=material)
        .aggregate(total=Sum('cantidad_asignada'))
        .get('total') or 0
    )

    AsignacionMaterial.objects.filter(material=material).update(cantidad_existente=total_asignada)

    material.cantidad_existente = total_asignada
    material.save(update_fields=['cantidad_existente'])
