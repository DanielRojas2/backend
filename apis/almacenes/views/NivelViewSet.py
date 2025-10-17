from rest_framework import viewsets
from ..models.Nivel import Nivel
from ..serializers.NivelSerializer import NivelSerializer

class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer
