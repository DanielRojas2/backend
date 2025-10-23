from rest_framework import serializers
from ..models.Material import Material
from ..models.PartidaPresupuestaria import PartidaPresupuestaria
from ..models.Presentacion import Presentacion
from ..models.UdM import UdM
from .PartidaPresupuestariaSerializer import PartidaPresupuestariaSerializer
from .PresentacionSerializer import PresentacionSerializer
from .UdMSerializer import UdMSerializer

class MaterialSerializer(serializers.ModelSerializer):
    # Campos de solo lectura (detallados)
    partida_detalle = PartidaPresupuestariaSerializer(source='partida', read_only=True)
    presentacion_detalle = PresentacionSerializer(source='presentacion', read_only=True)
    unidad_de_medida_detalle = UdMSerializer(source='unidad_de_medida', read_only=True)

    # Campos de escritura (solo IDs)
    partida = serializers.PrimaryKeyRelatedField(queryset=PartidaPresupuestaria.objects.all())
    presentacion = serializers.PrimaryKeyRelatedField(queryset=Presentacion.objects.all())
    unidad_de_medida = serializers.PrimaryKeyRelatedField(queryset=UdM.objects.all())

    class Meta:
        model = Material
        fields = '__all__'
        read_only_fields = ('creado', 'actualizado')
