import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from core.api.serializers import UserSerializer

User = get_user_model()


@pytest.mark.django_db
def test_user_serializer(create_user):
    """
    Test should be checked user serializer
    """
    user = create_user(
        username="user",
        email="test@example.com",
        name="John Doe",
        password="john123",
    )
    serializer = UserSerializer(user)
    data = serializer.data
    assert data["username"] == "user"
    assert data["email"] == "test@example.com"
    assert data["name"] == "John Doe"


@pytest.mark.django_db
def test_create_user_api(authenticated_test_user_client):
    response = authenticated_test_user_client.post(
        "/core/v1/users/",
        {
            "username": "user1",
            "email": "test1@example.com",
            "password": "password123",
        },
    )
    assert response.status_code == 201
    assert response.data["username"] == "user1"
    assert response.data["email"] == "test1@example.com"
