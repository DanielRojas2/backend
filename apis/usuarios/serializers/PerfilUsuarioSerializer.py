from rest_framework import serializers
from datetime import date
from ..models.PerfilUsuario import PerfilUsuario


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    cargo_nombre = serializers.CharField(source='cargo.cargo', read_only=True)
    extra_kwargs = {'password': {'write_only': True}}

    class Meta:
        model = PerfilUsuario
        fields = [
            'id', 'username', 'email', 'password',
            'nombre', 'apellido_paterno', 'apellido_materno',
            'usuario_activo', 'usuario_admin', 'alta', 'baja',
            'cargo', 'cargo_nombre'
        ]
        read_only_fields = ['alta']

    def create(self, validated_data):
        password = validated_data.pop('password')

        usuario = PerfilUsuario.objects.create_user(
            password=password,
            **validated_data
        )

        if usuario.usuario_activo and not usuario.baja:
            siguiente_anio = date.today().year + 1
            usuario.baja = date(siguiente_anio, 1, 10)

        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        # Actualizar campos excepto la contraseña
        validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if instance.usuario_activo and not instance.baja:
            siguiente_anio = date.today().year + 1
            instance.baja = date(siguiente_anio, 1, 10)

        instance.save()
        return instance
