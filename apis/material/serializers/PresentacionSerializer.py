from rest_framework import serializers
from ..models.Presentacion import Presentacion

class PresentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        fields = '__all__'
        read_only_fields = ('creado', 'actualizado')
