from rest_framework import viewsets
from ..models.PartidaPresupuestaria import PartidaPresupuestaria
from ..serializers.PartidaPresupuestariaSerializer import PartidaPresupuestariaSerializer

class PartidaPresupuestariaViewSet(viewsets.ModelViewSet):
    queryset = PartidaPresupuestaria.objects.all()
    serializer_class = PartidaPresupuestariaSerializer
