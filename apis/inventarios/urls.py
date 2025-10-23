from rest_framework.routers import DefaultRouter
from .views.AsignacionMaterialViewSet import AsignacionMaterialViewSet

router = DefaultRouter()
router.register(r'inventario-material', AsignacionMaterialViewSet, basename='inventario-material')

urlpatterns = router.urls
