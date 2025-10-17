from rest_framework import serializers
from ..models.Almacen import Almacen

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = '__all__'
        read_only_fields = ('creado', 'actualizado')
