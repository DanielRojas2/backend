from rest_framework import serializers
from ..models.Almacen import Almacen

class EstanteReporteSerializer(serializers.Serializer):
    nro_estante = serializers.IntegerField()
    cantidad_niveles = serializers.IntegerField()

class ReporteAlmacenSerializer(serializers.ModelSerializer):
    total_estantes = serializers.IntegerField()
    estantes = EstanteReporteSerializer(many=True, read_only=True)

    class Meta:
        model = Almacen
        fields = [
            'id', 'tipo_almacen', 'ubicacion',
            'total_estantes', 'estantes'
        ]
