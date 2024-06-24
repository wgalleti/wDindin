import pytest

from financial.api.serializers import CreditCardSerializerV1
from financial.models import CreditCard


@pytest.mark.django_db
def test_bank_serializer(
    create_test_credit_card,
):
    card = create_test_credit_card
    serializer = CreditCardSerializerV1(card)
    data = serializer.data
    assert data["name"] == "Card 1"
    assert data["expiration_date"] == "06/31"
    assert data["final_number"] == "1234"
    assert data["limit"] == 100
    assert data["flag"] == CreditCard.CreditCardFlag.MASTER


@pytest.mark.django_db
def test_create_creditcard_api(
    authenticated_test_user_client,
    create_test_bank,
):
    response = authenticated_test_user_client.post(
        "/api/v1/cards/",
        {
            "bank": create_test_bank.id,
            "name": "Card API",
            "final_number": "4321",
            "expiration_date": "07/31",
            "limit": 100,
            "flag": CreditCard.CreditCardFlag.MASTER,
        },
    )
    assert response.status_code == 201
    assert response.data["name"] == "Card API"
    assert response.data["expiration_date"] == "07/31"
    assert response.data["final_number"] == "4321"
    assert response.data["limit"] == 100
    assert response.data["flag"] == CreditCard.CreditCardFlag.MASTER


@pytest.mark.django_db
def test_update_creditcard_api(
    authenticated_test_user_client,
    create_test_credit_card,
):
    response = authenticated_test_user_client.patch(
        f"/api/v1/cards/{create_test_credit_card.id}/",
        {
            "name": "UPDATED",
        },
    )
    assert response.status_code == 200
    assert response.data["name"] == "UPDATED"


@pytest.mark.django_db
def test_delete_creditcard_api(
    authenticated_test_user_client,
    create_test_credit_card,
):
    response = authenticated_test_user_client.delete(
        f"/api/v1/cards/{create_test_credit_card.id}/",
    )
    assert response.status_code == 204
    assert CreditCard.objects.filter(pk=create_test_credit_card.id).exists() is False
