from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.PerfilUsuarioViewSet import PerfilUsuarioViewSet
from .views.AuthView import CustomTokenObtainPairView, CustomTokenRefreshView

router = DefaultRouter()
router.register(r'usuarios', PerfilUsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
    path('iniciar-sesion/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refrescar-token/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
