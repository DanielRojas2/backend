import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_creacion_usuario(api_client, usuario_admin):
    api_client.force_authenticate(user=usuario_admin)
    url = reverse("usuarios-list")

    data = {
        "username": "user1",
        "email": "user1@test.com",
        "password": "123456",
        "nombre": "User",
        "apellido_paterno": "Test"
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == 201
    assert "password" not in response.data
    assert response.data["usuario_activo"] is True
    assert response.data["baja"] is not None
