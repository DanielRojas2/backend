from rest_framework import viewsets
from ..models.Presentacion import Presentacion
from ..serializers.PresentacionSerializer import PresentacionSerializer

class PresentacionViewSet(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer
