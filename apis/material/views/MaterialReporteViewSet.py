from rest_framework import viewsets
from ..models.Material import Material
from ..serializers.MaterialReporteSerializer import MaterialReporteSerializer


class MaterialReporteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Material.objects.select_related(
        'partida', 'presentacion', 'unidad_de_medida'
    ).all()
    serializer_class = MaterialReporteSerializer
