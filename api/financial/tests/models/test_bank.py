import pytest
from django.core.exceptions import ValidationError

from financial.models import Bank


@pytest.mark.django_db
def test_create_bank(create_test_user, create_test_bank):
    """
    Test should be able to create bank account
    """

    assert create_test_bank.name == "Test bank"
    assert create_test_bank.code == "test"
    assert create_test_bank.created_by == create_test_user


@pytest.mark.django_db
def test_create_bank_without_code(create_test_user):
    """
    Test should be raise error when bank code is missing
    """
    with pytest.raises(ValidationError):
        Bank.objects.create(
            name="Test bank",
            created_by=create_test_user,
        )


@pytest.mark.django_db
def test_create_bank_unique_code(create_test_user, create_test_bank):
    with pytest.raises(ValidationError):
        Bank.objects.create(
            name="Test bank 2",
            code="test",
            created_by=create_test_user,
        )
