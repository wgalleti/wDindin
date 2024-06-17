import pytest

from financial.models import BankAccount


@pytest.mark.django_db
def test_create_bank_account(authenticated_test_user_client, create_test_bank):
    response = authenticated_test_user_client.post(
        "/api/v1/accounts/",
        {
            "bank": str(create_test_bank.id),
            "name": "Account Test",
            "initial_balance": 100,
            "account_type": str(BankAccount.BankAccountType.CHECKING),
        },
    )
    assert response.status_code == 201
    assert response.data["name"] == "Account Test"
    assert response.data["initial_balance"] == 100
    assert response.data["bank"] == create_test_bank.id
    assert response.data["account_type"] == BankAccount.BankAccountType.CHECKING


@pytest.mark.django_db
def test_list_bank_accounts(authenticated_test_user_client, create_test_account):
    response = authenticated_test_user_client.get(
        "/api/v1/accounts/",
    )
    assert response.status_code == 200
    assert isinstance(response.data["data"], list)
    assert response.data["total"] == 1


@pytest.mark.django_db
def test_update_bank_account(authenticated_test_user_client, create_test_account):
    response = authenticated_test_user_client.patch(
        f"/api/v1/accounts/{create_test_account.id}/",
        {
            "name": "Account Test UPDATED",
        },
    )
    assert response.status_code == 200
    assert response.data["name"] != create_test_account.name
    assert response.data["initial_balance"] == create_test_account.initial_balance


@pytest.mark.django_db
def test_delete_bank_account(authenticated_test_user_client, create_test_account):
    response = authenticated_test_user_client.delete(
        f"/api/v1/accounts/{create_test_account.id}/",
    )
    assert response.status_code == 204
    assert BankAccount.objects.filter(id=create_test_account.id).exists() is False
