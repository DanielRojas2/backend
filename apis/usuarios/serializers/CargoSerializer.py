from rest_framework import serializers
from ..models.Cargo import Cargo

class CargoSerializer(serializers.ModelSerializer):
    departamento = serializers.CharField(source='departamento.departamento', read_only=True)
    unidad = serializers.CharField(source='unidad.unidad', read_only=True)
    rol = serializers.CharField(source='rol.rol', read_only=True)

    class Meta:
        model = Cargo
        fields = ['id', 'cargo', 'departamento', 'unidad', 'rol']