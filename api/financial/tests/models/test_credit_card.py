import pytest
from cryptography.fernet import Fernet
from django.conf import settings
from django.core.exceptions import ValidationError

from financial.models import CreditCard


@pytest.mark.django_db
def test_create_credit_card(
    create_test_credit_card,
):
    pass


@pytest.mark.django_db
def test_create_credit_card_wrong_expiration(
    create_test_bank,
    create_test_user,
):
    with pytest.raises(ValidationError):
        CreditCard.objects.get_or_create(
            bank=create_test_bank,
            name="Card 1",
            final_number="1234",
            _expiration_date=Fernet(settings.CRYPTOGRAPHY_KEY).encrypt(b"0631"),
            limit=100,
            flag=CreditCard.CreditCardFlag.MASTER,
            created_by=create_test_user,
        )


@pytest.mark.django_db
def test_create_credit_card_wrong_final_number(
    create_test_bank,
    create_test_user,
):
    with pytest.raises(ValidationError):
        CreditCard.objects.get_or_create(
            bank=create_test_bank,
            name="Card 1",
            final_number="12345",
            _expiration_date=Fernet(settings.CRYPTOGRAPHY_KEY).encrypt(b"06/31"),
            limit=100,
            flag=CreditCard.CreditCardFlag.MASTER,
            created_by=create_test_user,
        )
