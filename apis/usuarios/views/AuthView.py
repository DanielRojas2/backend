from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from ..models.PerfilUsuario import PerfilUsuario
from ..serializers.PerfilUsuarioSerializer import PerfilUsuarioSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        usuario = authenticate(username=username, password=password)
        if not usuario:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        if not usuario.usuario_activo:
            return Response({"error": "El usuario está inactivo"}, status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(usuario)

        data = PerfilUsuarioSerializer(usuario).data
        data.update({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
        return Response(data, status=status.HTTP_200_OK)


class CustomTokenRefreshView(TokenRefreshView):
    """
    Permite refrescar el token sin volver a loguearse
    """
    pass
