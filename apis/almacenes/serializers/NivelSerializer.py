from rest_framework import serializers
from ..models.Nivel import Nivel

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'
        read_only_fields = ('creado', 'actualizado')
        