from rest_framework import serializers
from ..models.AsignacionMaterial import AsignacionMaterial

class AsignacionMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionMaterial
        fields = '__all__'
        read_only = ['creado', 'actualizado']
