from rest_framework import viewsets
from ..models.NivelEstante import NivelEstante
from ..serializers.NivelEstanteSerializer import NivelEstanteSerializer

class NivelEstanteViewSet(viewsets.ModelViewSet):
    queryset = NivelEstante.objects.all()
    serializer_class = NivelEstanteSerializer
