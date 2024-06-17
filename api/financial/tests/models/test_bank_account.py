import pytest

from financial.models import BankAccount


@pytest.mark.django_db
def test_create_bank_account(create_test_bank, create_test_user):
    BankAccount.objects.create(
        bank=create_test_bank,
        name="Account Test",
        initial_balance=100,
        account_type=BankAccount.BankAccountType.CHECKING,
        created_by=create_test_user,
    )


@pytest.mark.django_db
def test_create_without_defaults(create_test_bank, create_test_user):
    account = BankAccount.objects.create(
        bank=create_test_bank,
        name="Account Test",
        created_by=create_test_user,
    )

    assert account.initial_balance == 0
    assert account.account_type == BankAccount.BankAccountType.CHECKING
