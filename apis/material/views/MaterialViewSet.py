from rest_framework import viewsets
from ..models.Material import Material
from ..serializers.MaterialSerializer import MaterialSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.select_related(
        'partida', 'presentacion', 'unidad_de_medida'
    ).all()
    serializer_class = MaterialSerializer
