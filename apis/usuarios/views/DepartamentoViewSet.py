from rest_framework import viewsets
from ..models.Departamento import Departamento
from ..serializers.DepartamentoSerializer import DepartamentoSerializer

class DepartamentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
