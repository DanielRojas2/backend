from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.PerfilUsuarioViewSet import PerfilUsuarioViewSet
from .views.CargoViewSet import CargoViewSet
from .views.DepartamentoViewSet import DepartamentoViewSet
from .views.RolViewSet import RolViewSet
from .views.UnidadViewSet import UnidadViewSet
from .views.AuthView import CustomTokenObtainPairView, CustomTokenRefreshView

router = DefaultRouter()
router.register(r'usuarios', PerfilUsuarioViewSet, basename='usuarios')
router.register(r'cargos', CargoViewSet, basename='cargos')
router.register(r'departamentos', DepartamentoViewSet, basename='departamentos')
router.register(r'roles', RolViewSet, basename='roles')
router.register(r'unidades', UnidadViewSet, basename='unidades')

urlpatterns = router.urls

urlpatterns += [
    path('iniciar-sesion/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refrescar-token/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
