from rest_framework.routers import DefaultRouter
from .views.PartidaPresupuestariaViewSet import PartidaPresupuestariaViewSet
from .views.PresentacionViewSet import PresentacionViewSet
from .views.UdMViewSet import UdMViewSet
from .views.MaterialViewSet import MaterialViewSet
from .views.MaterialReporteViewSet import MaterialReporteViewSet

router = DefaultRouter()

router.register(r'partidas', PartidaPresupuestariaViewSet)
router.register(r'presentaciones', PresentacionViewSet)
router.register(r'unidades-medida', UdMViewSet)
router.register(r'materiales', MaterialViewSet)
router.register(r'reporte-materiales', MaterialReporteViewSet, basename='reporte-materiales')

urlpatterns = router.urls
