from rest_framework.routers import DefaultRouter
from .views.AlmacenViewSet import AlmacenViewSet
from .views.EstanteViewSet import EstanteViewSet
from .views.NivelViewSet import NivelViewSet
from .views.NivelEstanteViewSet import NivelEstanteViewSet
from .views.ReporteAlmacenViewSet import ReporteAlmacenViewSet

router = DefaultRouter()

router.register(r'almacenes', AlmacenViewSet)
router.register(r'estantes', EstanteViewSet)
router.register(r'niveles', NivelViewSet)
router.register(r'nivel-estantes', NivelEstanteViewSet)
router.register(r'reporte-almacenes', ReporteAlmacenViewSet, basename='reporte-almacenes')

urlpatterns = router.urls
