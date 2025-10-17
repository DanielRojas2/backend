from rest_framework import serializers
from ..models.Estante import Estante

class EstanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estante
        fields = '__all__'
        read_only_fields = ('creado', 'actualizado')
        