from rest_framework.routers import DefaultRouter
from .views import NotificacionViewSet

router = DefaultRouter()
router.register('notificaciones', NotificacionViewSet, basename='notificaciones')

urlpatterns = router.urls
