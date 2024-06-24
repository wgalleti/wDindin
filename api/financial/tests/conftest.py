import pytest
from cryptography.fernet import Fernet
from django.conf import settings
from django.utils import timezone

from financial.models import (
    Bank,
    Category,
    TransactionType,
    BankAccount,
    Transaction,
    CreditCard,
)


@pytest.fixture
def create_test_bank(create_test_user):
    bank, _ = Bank.objects.update_or_create(
        name="Test bank",
        code="test",
        defaults=dict(
            created_by=create_test_user,
        ),
    )
    return bank


@pytest.fixture
def create_test_category_expense(create_test_user):
    category, _ = Category.objects.update_or_create(
        name="Category Test Expense",
        icon="fa fa-test",
        transaction_type=TransactionType.EXPENSE,
        created_by=create_test_user,
    )
    return category


@pytest.fixture
def create_test_category_income(create_test_user):
    category, _ = Category.objects.update_or_create(
        name="Category Test Incoming",
        icon="fa fa-test",
        transaction_type=TransactionType.INCOME,
        created_by=create_test_user,
    )
    return category


@pytest.fixture
def create_test_account(create_test_user, create_test_bank):
    account, _ = BankAccount.objects.get_or_create(
        bank=create_test_bank,
        name="Account Test",
        defaults=dict(
            initial_balance=100,
            account_type=BankAccount.BankAccountType.CHECKING,
            created_by=create_test_user,
        ),
    )
    return account


@pytest.fixture
def create_test_credit_card(create_test_user, create_test_bank):
    card, _ = CreditCard.objects.get_or_create(
        bank=create_test_bank,
        name="Card 1",
        final_number="1234",
        _expiration_date=Fernet(settings.CRYPTOGRAPHY_KEY).encrypt(b"06/31"),
        defaults=dict(
            limit=100,
            flag=CreditCard.CreditCardFlag.MASTER,
            created_by=create_test_user,
        ),
    )
    return card


@pytest.fixture
def create_test_transaction(
    create_test_user,
    create_test_account,
    create_test_category_expense,
):
    return Transaction.objects.create(
        date=timezone.now(),
        bank_account=create_test_account,
        category=create_test_category_expense,
        description=f"Transaction for {create_test_category_expense.name}",
        value=1000,
        created_by=create_test_user,
    )
