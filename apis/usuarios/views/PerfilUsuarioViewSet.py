from datetime import date, timedelta
from django.db.models import Prefetch
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.PerfilUsuario import PerfilUsuario
from ..models.UsuarioLog import UsuarioLog
from ..permissions import RolPermission
from ..serializers.PerfilUsuarioSerializer import PerfilUsuarioSerializer
from ..serializers.UsuarioLogSerializer import UsuarioLogSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all().select_related(
        'cargo__departamento', 'cargo__unidad', 'cargo__rol'
    )
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [IsAuthenticated, RolPermission]

    allowed_roles = ['encargado de sistemas']

    def create(self, request, *args, **kwargs):
        self.allowed_roles = ['encargado de sistemas']
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()

        UsuarioLog.objects.create(usuario=usuario, accion="creado")

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        self.allowed_roles = ['encargado de sistemas']
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data.copy()

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def cambiar_estado(self, request, pk=None):
        self.allowed_roles = ['encargado de sistemas']
        usuario = self.get_object()
        estado = request.data.get("usuario_activo")

        if estado is None:
            return Response(
                {"error": "Debe enviar el campo 'usuario_activo' (true/false)."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        estado_bool = str(estado).lower() in ["true", "1", "t", "yes", "on"]
        hoy = date.today()
        siguiente_anio = hoy.year + 1

        if usuario.usuario_activo == estado_bool:
            return Response(
                {"detalle": f"El usuario '{usuario.username}' ya estaba {'activo' if estado_bool else 'inactivo'}."},
                status=status.HTTP_200_OK,
            )

        if not estado_bool:
            usuario.dar_baja_manual()
            UsuarioLog.objects.create(usuario=usuario, accion="desactivado")
            return Response(
                {"detalle": f"Usuario '{usuario.username}' dado de baja correctamente."},
                status=status.HTTP_200_OK,
            )

        usuario.usuario_activo = True
        usuario.baja = date(siguiente_anio, 1, 10)
        usuario.save()
        UsuarioLog.objects.create(usuario=usuario, accion="activado")

        return Response(
            {"detalle": f"Usuario '{usuario.username}' reactivado correctamente."},
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=['get'])
    def reporte_completo(self, request):
        self.allowed_roles = ['encargado de sistemas']
        usuarios = PerfilUsuario.objects.select_related(
            'cargo__departamento', 'cargo__unidad', 'cargo__rol'
        )
        data = []
        for u in usuarios:
            data.append({
                "id": u.id,
                "nombre_completo": str(u),
                "username": u.username,
                "email": u.email,
                "activo": u.usuario_activo,
                "baja": u.baja,
                "departamento": u.cargo.departamento.departamento if u.cargo else None,
                "unidad": u.cargo.unidad.unidad if u.cargo else None,
                "rol": u.cargo.rol.rol if u.cargo else None,
                "cargo": u.cargo.cargo if u.cargo else None,
            })
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def reporte_auditoria(self, request):
        self.allowed_roles = ['encargado de sistemas']
        logs = UsuarioLog.objects.select_related('usuario').order_by('-fecha')
        serializer = UsuarioLogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def proximos_a_vencer(self, request):
        self.allowed_roles = ['encargado de sistemas']
        hoy = date.today()
        limite = hoy + timedelta(days=30)
        usuarios = PerfilUsuario.objects.filter(
            usuario_activo=True, baja__range=(hoy, limite)
        )
        serializer = self.get_serializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
