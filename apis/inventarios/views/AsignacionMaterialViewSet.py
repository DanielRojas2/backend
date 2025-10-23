from rest_framework import viewsets
from ..models.AsignacionMaterial import AsignacionMaterial
from ..serializers.AsignacionMaterialSerializer import AsignacionMaterialSerializer

class AsignacionMaterialViewSet(viewsets.ModelViewSet):
    queryset = AsignacionMaterial.objects.all()
    serializer_class = AsignacionMaterialSerializer
