from rest_framework import serializers
from ..models.Material import Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
        read_only_fields = ('creado', 'actualizado')
