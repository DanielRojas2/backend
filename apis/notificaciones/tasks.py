from celery import shared_task
from datetime import date, timedelta
from django.db.models import Q
from ..usuarios.models.PerfilUsuario import PerfilUsuario
from .models import Notificacion

@shared_task
def generar_notificaciones_baja():
    hoy = date.today()
    fecha_objetivo = hoy + timedelta(days=3)

    usuarios_proximos = PerfilUsuario.objects.filter(
        usuario_activo=True,
        baja=fecha_objetivo
    )

    if not usuarios_proximos.exists():
        return "No hay usuarios próximos a baja."

    for usuario in usuarios_proximos:
        Notificacion.objects.create(
            usuario=usuario,
            titulo="Aviso de Baja Próxima",
            mensaje=f"Tu cuenta será dada de baja el día {usuario.baja}. "
                    f"Contacta con el administrador si crees que es un error."
        )

    encargados = PerfilUsuario.objects.filter(
        Q(cargo__rol__rol__iexact='encargado de sistemas')
    )

    for encargado in encargados:
        Notificacion.objects.create(
            usuario=encargado,
            titulo="Usuarios próximos a baja",
            mensaje=f"Existen {usuarios_proximos.count()} usuario(s) "
                    f"cuya fecha de baja es dentro de 3 días."
        )

    return f"Notificaciones generadas para {usuarios_proximos.count()} usuarios."
