import decimal
from datetime import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from core.mixins.models import (
    BaseModelUUID,
    BaseModelCreatedData,
)
from cryptography.fernet import Fernet
from django.db.models import Sum, Case, When, F, DecimalField


class Bank(
    BaseModelUUID,
    BaseModelCreatedData,
):
    name = models.CharField(
        max_length=255,
    )
    code = models.CharField(
        max_length=100,
        unique=True,
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class BankAccount(
    BaseModelUUID,
    BaseModelCreatedData,
):
    class BankAccountType(models.TextChoices):
        CHECKING = "CHECKING", "Checking"
        INVESTMENT = "INVESTMENT", "Investment"
        CASH = "CASH", "Cash"

    bank = models.ForeignKey(
        "financial.Bank",
        on_delete=models.CASCADE,
        related_name="accounts",
    )
    name = models.CharField(
        max_length=255,
    )
    initial_balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    account_type = models.CharField(
        max_length=30,
        choices=BankAccountType.choices,
        default=BankAccountType.CHECKING,
    )

    def __str__(self):
        return f"{self.bank.name} - {self.name} ({self.get_account_type_display()})"


class CreditCard(BaseModelUUID, BaseModelCreatedData):
    class CreditCardFlag(models.TextChoices):
        MASTER = "MASTER", "Master"
        VISA = "VISA", "Visa"
        OTHER = "OTHER", "Other"

    bank = models.ForeignKey(
        "financial.Bank",
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    name = models.CharField(
        max_length=255,
    )
    flag = models.CharField(
        max_length=30,
        choices=CreditCardFlag.choices,
        default=CreditCardFlag.MASTER,
    )
    final_number = models.CharField(
        max_length=4,
    )
    _expiration_date = models.BinaryField()
    limit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    @property
    def expiration_date(self):
        f = Fernet(settings.CRYPTOGRAPHY_KEY)
        return f.decrypt(self._expiration_date).decode("utf-8")

    @expiration_date.setter
    def expiration_date(self, value):
        f = Fernet(settings.CRYPTOGRAPHY_KEY)
        self._expiration_date = f.encrypt(value.encode("utf-8"))

    @property
    def balance(self):
        transactions_value = (
            self.transactions.all()
            .aggregate(
                balance=Sum(
                    Case(
                        When(category__transaction_type="INCOME", then=F("value")),
                        When(
                            category__transaction_type="EXPENSE", then=F("value") * -1
                        ),
                        output_field=DecimalField(),
                    )
                )
            )
            .get("balance")
        )

        if transactions_value is None:
            return self.limit

        return self.limit - transactions_value

    def save(self, *args, **kwargs):
        if not self.final_number.isdigit() or len(self.final_number) != 4:
            raise ValidationError("Last four digits must be exactly 4 numbers.")

        if (
            not self.expiration_date
            or len(self.expiration_date) != 5
            or self.expiration_date[2] != "/"
        ):
            raise ValidationError("Expiration date must be in MM/YY format.")

        super().save(*args, **kwargs)


class TransactionType(models.TextChoices):
    INCOME = "INCOME", "Income"
    EXPENSE = "EXPENSE", "Expense"


class Category(
    BaseModelUUID,
    BaseModelCreatedData,
):
    name = models.CharField(
        max_length=255,
    )
    icon = models.CharField(
        max_length=100,
    )
    transaction_type = models.CharField(
        max_length=30,
        choices=TransactionType.choices,
        default=TransactionType.EXPENSE,
    )

    @property
    def value(self):
        return sum(self.transactions.all().values_list("value", flat=True))


class Transaction(
    BaseModelUUID,
    BaseModelCreatedData,
):
    date = models.DateField()
    bank_account = models.ForeignKey(
        "financial.BankAccount",
        on_delete=models.CASCADE,
        related_name="transactions",
        null=True,
        blank=True,
    )
    credit_card = models.ForeignKey(
        "financial.CreditCard",
        on_delete=models.CASCADE,
        related_name="transactions",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "financial.Category",
        on_delete=models.CASCADE,
        related_name="transactions",
        null=True,
        blank=True,
    )
    description = models.TextField()
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(decimal.Decimal("0.01")),
        ],
    )

    def _credit_card_validations(self):
        if not self.credit_card:
            return

        if self.category.transaction_type == TransactionType.INCOME:
            raise ValidationError("Credit Card has not receive income")

        if self.credit_card.balance <= 0:
            raise ValidationError("Credit Card has not limit")

    def save(self, *args, **kwargs):
        self.full_clean()

        self._credit_card_validations()

        super().save(*args, **kwargs)

    @property
    def transaction_type(self):
        return self.category.transaction_type
