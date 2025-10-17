from rest_framework import serializers
from ..models.UsuarioLog import UsuarioLog

class UsuarioLogSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = UsuarioLog
        fields = ['id', 'usuario', 'usuario_nombre', 'accion', 'fecha', 'motivo']
