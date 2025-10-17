from rest_framework import serializers
from ..models.PartidaPresupuestaria import PartidaPresupuestaria

class PartidaPresupuestariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidaPresupuestaria
        fields = '__all__'
        read_only_fields = ('creado', 'actualizado')