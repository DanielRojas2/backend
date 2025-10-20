from rest_framework import viewsets
from ..models.Unidad import Unidad
from ..serializers.UnidadSerializer import UnidadSerializer

class UnidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
