import pytest

from financial.models import TransactionType, Category


@pytest.mark.django_db
def test_create_category(authenticated_test_user_client):
    response = authenticated_test_user_client.post(
        "/api/v1/categories/",
        {
            "name": "Category Test",
            "icon": "fa fa-test",
        },
    )
    assert response.status_code == 201
    assert response.data["name"] == "Category Test"
    assert response.data["transaction_type"] == TransactionType.EXPENSE


@pytest.mark.django_db
def test_list_categories(
    authenticated_test_user_client,
    create_test_category_income,
    create_test_category_expense,
):
    response = authenticated_test_user_client.get(
        "/api/v1/categories/",
    )
    assert response.status_code == 200
    assert isinstance(response.data["data"], list)
    assert response.data["total"] == 2


@pytest.mark.django_db
def test_update_category(authenticated_test_user_client, create_test_category_expense):
    response = authenticated_test_user_client.patch(
        f"/api/v1/categories/{create_test_category_expense.id}/",
        {
            "name": "UPDATED",
        },
    )
    assert response.status_code == 200
    assert response.data["name"] != create_test_category_expense.name


@pytest.mark.django_db
def test_delete_category(authenticated_test_user_client, create_test_category_expense):
    response = authenticated_test_user_client.delete(
        f"/api/v1/categories/{create_test_category_expense.id}/",
    )
    assert response.status_code == 204
    assert Category.objects.filter(id=create_test_category_expense.id).exists() is False
