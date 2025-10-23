import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

Usuario = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def usuario_admin(db):
    usuario = Usuario.objects.create_user(
        username="admin",
        email="admin@test.com",
        password="admin123",
        nombre="Admin",
        apellido_paterno="Test",
    )
    usuario.usuario_admin = True
    usuario.save()
    return usuario
