from rest_framework import serializers
from ..models.NivelEstante import NivelEstante

class ReporteAlmacenSerializer(serializers.ModelSerializer):
    nivel_estante = serializers.SerializerMethodField()
    almacen = serializers.CharField(
        source='estante.almacen.id', read_only=True
    )
    ubicacion = serializers.CharField(
        source='estante.almacen.ubicacion', read_only=True
    )
    tipo_almacen = serializers.CharField(
        source='estante.almacen.tipo_almacen', read_only=True
    )

    class Meta:
        model = NivelEstante
        fields = [
            'id',
            'nivel_estante',
            'almacen',
            'ubicacion',
            'tipo_almacen'
        ]

    def get_nivel_estante(self, obj):
        return f"Nivel {obj.nivel.nro_nivel} - Estante {obj.estante.nro_estante}"
