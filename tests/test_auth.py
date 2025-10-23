import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_login_correcto(api_client, usuario_admin):
    url = reverse("token_obtain_pair")
    response = api_client.post(url, {
        "username": "admin",
        "password": "admin123"
    })

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data
