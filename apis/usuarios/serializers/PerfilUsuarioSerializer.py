from rest_framework import serializers
from datetime import date
from ..models.PerfilUsuario import PerfilUsuario
from .CargoSerializer import CargoSerializer

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    cargo_detalle = CargoSerializer(source='cargo', read_only=True)

    class Meta:
        model = PerfilUsuario
        fields = [
            'id', 'username', 'email', 'password',
            'nombre', 'apellido_paterno', 'apellido_materno',
            'usuario_activo', 'usuario_admin', 'alta', 'baja',
            'cargo', 'cargo_detalle',
        ]
        read_only_fields = ['alta']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def to_representation(self, instance):
        """Ocultar password al hacer GET automáticamente"""
        rep = super().to_representation(instance)
        rep.pop('password', None)
        return rep

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        usuario = PerfilUsuario.objects.create_user(password=password, **validated_data)

        if usuario.usuario_activo and not usuario.baja:
            siguiente_anio = date.today().year + 1
            usuario.baja = date(siguiente_anio, 1, 10)
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        if instance.usuario_activo and not instance.baja:
            siguiente_anio = date.today().year + 1
            instance.baja = date(siguiente_anio, 1, 10)

        instance.save()
        return instance