from rest_framework import serializers
from ..models.NivelEstante import NivelEstante

class NivelEstanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelEstante
        fields = '__all__'
        read_only_fields = ('creado', 'actualizado')
        