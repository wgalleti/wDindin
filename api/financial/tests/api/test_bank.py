import pytest

from financial.api.serializers import BankSerializer
from financial.models import Bank


@pytest.mark.django_db
def test_bank_serializer(create_test_user):
    bank = Bank(
        name="Bank Test",
        code="test",
        created_by=create_test_user,
    )
    serializer = BankSerializer(bank)
    data = serializer.data
    assert data["name"] == "Bank Test"
    assert data["code"] == "test"


@pytest.mark.django_db
def test_create_bank_api(authenticated_test_user_client):
    response = authenticated_test_user_client.post(
        "/api/v1/banks/",
        {
            "name": "Bank Test",
            "code": "test",
        },
    )
    assert response.status_code == 201
    assert response.data["name"] == "Bank Test"
    assert response.data["code"] == "test"


@pytest.mark.django_db
def test_update_bank_api(authenticated_test_user_client, create_test_bank):
    response = authenticated_test_user_client.patch(
        f"/api/v1/banks/{create_test_bank.id}/",
        {
            "name": "Bank Test UPDATED",
        },
    )
    assert response.status_code == 200
    assert response.data["name"] == "Bank Test UPDATED"
    assert response.data["code"] == "test"


@pytest.mark.django_db
def test_delete_bank_api(authenticated_test_user_client, create_test_bank):
    response = authenticated_test_user_client.delete(
        f"/api/v1/banks/{create_test_bank.id}/",
    )
    assert response.status_code == 204
    assert Bank.objects.filter(pk=create_test_bank.id).exists() is False
