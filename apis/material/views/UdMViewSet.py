from rest_framework import viewsets
from ..models.UdM import UdM
from ..serializers.UdMSerializer import UdMSerializer

class UdMViewSet(viewsets.ModelViewSet):
    queryset = UdM.objects.all()
    serializer_class = UdMSerializer
