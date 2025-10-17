from rest_framework import viewsets
from ..models.Almacen import Almacen
from ..serializers.AlmacenSerializer import AlmacenSerializer

class AlmacenViewSet(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer
