import pytest
from django.utils import timezone

from financial.models import Transaction


@pytest.mark.django_db
def test_create_transaction(
    authenticated_test_user_client, create_test_account, create_test_category_expense
):
    response = authenticated_test_user_client.post(
        "/api/v1/transactions/",
        {
            "date": timezone.now().strftime("%Y-%m-%d"),
            "bank_account": create_test_account.id,
            "category": create_test_category_expense.id,
            "description": f"Transaction for {create_test_category_expense.name}",
            "value": 1000,
        },
    )
    assert response.status_code == 201
    assert response.data["date"] == timezone.now().strftime("%Y-%m-%d")
    assert response.data["bank_account"] == create_test_account.id
    assert response.data["category"] == create_test_category_expense.id
    assert (
        response.data["description"]
        == f"Transaction for {create_test_category_expense.name}"
    )
    assert response.data["value"] == 1000


@pytest.mark.django_db
def test_list_transactions(
    authenticated_test_user_client,
    create_test_transaction,
):
    response = authenticated_test_user_client.get(
        "/api/v1/transactions/",
    )
    assert response.status_code == 200
    assert isinstance(response.data["data"], list)
    assert response.data["total"] == 1


@pytest.mark.django_db
def test_update_transaction(
    authenticated_test_user_client,
    create_test_transaction,
):
    response = authenticated_test_user_client.patch(
        f"/api/v1/transactions/{create_test_transaction.id}/",
        {
            "description": "UPDATED",
        },
    )
    assert response.status_code == 200
    assert response.data["description"] != create_test_transaction.description


@pytest.mark.django_db
def test_delete_transaction(authenticated_test_user_client, create_test_transaction):
    response = authenticated_test_user_client.delete(
        f"/api/v1/transactions/{create_test_transaction.id}/",
    )
    assert response.status_code == 204
    assert Transaction.objects.filter(id=create_test_transaction.id).exists() is False
