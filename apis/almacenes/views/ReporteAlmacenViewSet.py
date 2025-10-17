from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models.NivelEstante import NivelEstante
from ..serializers.ReporteAlmacenSerializer import ReporteAlmacenSerializer

class ReporteAlmacenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NivelEstante.objects.select_related(
        'nivel', 'estante', 'estante__almacen'
    ).all()
    serializer_class = ReporteAlmacenSerializer
