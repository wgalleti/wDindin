import decimal

import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone

from financial.models import Transaction


@pytest.mark.django_db
def test_transaction_create(
    create_test_user,
    create_test_category_expense,
    create_test_category_income,
    create_test_account,
):
    for i in range(10):
        category = (
            create_test_category_income if i % 2 == 0 else create_test_category_expense
        )
        value = decimal.Decimal(
            10 * i + 0.01,
        ).quantize(
            decimal.Decimal(".01"),
            rounding=decimal.ROUND_DOWN,
        )

        Transaction.objects.create(
            date=timezone.now(),
            bank_account=create_test_account,
            category=category,
            description=f"Transaction {i} for {category.name}",
            value=value,
            created_by=create_test_user,
        )


@pytest.mark.django_db
def test_transaction_validators(
    create_test_user,
    create_test_category_expense,
    create_test_account,
):

    with pytest.raises(ValidationError):
        Transaction.objects.create(
            date=timezone.now(),
            bank_account=create_test_account,
            category=create_test_category_expense,
            description=f"Transaction for {create_test_category_expense.name}",
            value=decimal.Decimal("0"),
            created_by=create_test_user,
        )

        Transaction.objects.create(
            date=timezone.now(),
            bank_account=create_test_account,
            category=create_test_category_expense,
            description=f"Transaction for {create_test_category_expense.name}",
            value=decimal.Decimal("-1"),
            created_by=create_test_user,
        )

        Transaction.objects.create()


@pytest.mark.django_db
def test_transaction_custom_properties(
    create_test_user,
    create_test_category_expense,
    create_test_account,
):
    transaction = Transaction.objects.create(
        date=timezone.now(),
        bank_account=create_test_account,
        category=create_test_category_expense,
        description=f"Transaction for {create_test_category_expense.name}",
        value=decimal.Decimal("1000"),
        created_by=create_test_user,
    )

    assert (
        transaction.transaction_type.value
        == create_test_category_expense.transaction_type
    )
