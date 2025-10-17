from rest_framework import serializers
from ..models.UdM import UdM

class UdMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UdM
        fields = '__all__'
        read_only_fields = ('creado', 'actualizado')
