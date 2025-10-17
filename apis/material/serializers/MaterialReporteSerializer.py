from rest_framework import serializers
from ..models.Material import Material
from ..models.PartidaPresupuestaria import PartidaPresupuestaria
from ..models.Presentacion import Presentacion
from ..models.UdM import UdM

class PartidaPresupuestariaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidaPresupuestaria
        exclude = ('creado', 'actualizado')


class PresentacionDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        exclude = ('creado', 'actualizado')


class UdMDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UdM
        exclude = ('creado', 'actualizado')


class MaterialReporteSerializer(serializers.ModelSerializer):
    partida = PartidaPresupuestariaDetalleSerializer()
    presentacion = PresentacionDetalleSerializer()
    unidad_de_medida = UdMDetalleSerializer()

    class Meta:
        model = Material
        exclude = ('creado', 'actualizado')