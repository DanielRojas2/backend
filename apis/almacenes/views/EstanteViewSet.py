from rest_framework import viewsets
from ..models.Estante import Estante
from ..serializers.EstanteSerializer import EstanteSerializer

class EstanteViewSet(viewsets.ModelViewSet):
    queryset = Estante.objects.all()
    serializer_class = EstanteSerializer
