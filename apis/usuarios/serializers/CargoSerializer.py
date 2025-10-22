from rest_framework import serializers
from ..models.Cargo import Cargo
from ..models.Departamento import Departamento
from ..models.Unidad import Unidad
from ..models.Rol import Rol

class CargoSerializer(serializers.ModelSerializer):
    departamento_nombre = serializers.CharField(source='departamento.departamento', read_only=True)
    unidad_nombre = serializers.CharField(source='unidad.unidad', read_only=True)
    rol_nombre = serializers.CharField(source='rol.rol', read_only=True)

    departamento = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())
    unidad = serializers.PrimaryKeyRelatedField(queryset=Unidad.objects.all())
    rol = serializers.PrimaryKeyRelatedField(queryset=Rol.objects.all())

    class Meta:
        model = Cargo
        fields = ['id', 'cargo', 'departamento', 'departamento_nombre', 'unidad', 'unidad_nombre', 'rol', 'rol_nombre']
