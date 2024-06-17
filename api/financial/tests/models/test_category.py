import pytest
from financial.models import Category, TransactionType


@pytest.mark.django_db
def test_create_category(create_test_category_expense, create_test_category_income):
    pass


@pytest.mark.django_db
def test_create_category_without_defaults(create_test_user):
    category = Category.objects.create(
        name="Category Test",
        created_by=create_test_user,
    )

    assert category.transaction_type == TransactionType.EXPENSE


@pytest.mark.django_db
def test_custom_property_value(create_test_user):
    category = Category.objects.create(
        name="Category Test",
        created_by=create_test_user,
    )

    assert category.value == 0
