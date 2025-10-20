from rest_framework import viewsets
from ..models.Rol import Rol
from ..serializers.RolSerializer import RolSerializer

class RolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
