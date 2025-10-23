from rest_framework import viewsets
from rest_framework.response import Response
from ..models.Almacen import Almacen
from ..models.Estante import Estante
from ..serializers.ReporteAlmacenSerializer import ReporteAlmacenSerializer

class ReporteAlmacenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = ReporteAlmacenSerializer

    def list(self, request):
        almacenes = self.get_queryset()
        data = [self._get_almacen_data(a) for a in almacenes]
        return Response(data)

    def retrieve(self, request, pk=None):
        try:
            almacen = self.get_queryset().get(pk=pk)
        except Almacen.DoesNotExist:
            return Response({"detail": "Almacén no encontrado."}, status=404)
        data = self._get_almacen_data(almacen)
        return Response(data)

    def _get_almacen_data(self, almacen):
        estantes = almacen.estantes_almacen.all()
        estantes_data = [
            {
                "nro_estante": e.nro_estante,
                "cantidad_niveles": e.estante_nivel.count()
            }
            for e in estantes
        ]

        return {
            "id": almacen.id,
            "tipo_almacen": almacen.tipo_almacen,
            "ubicacion": almacen.ubicacion,
            "total_estantes": estantes.count(),
            "estantes": estantes_data
        }
