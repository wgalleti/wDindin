from django.db import models

from core.mixins.models import BaseModelUUID, BaseModelCreatedData


class Bank(
    BaseModelUUID,
    BaseModelCreatedData,
):
    name = models.CharField(
        max_length=255,
    )
    code = models.CharField(
        max_length=100,
    )


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
        default=TransactionType.INCOME,
    )


class Transaction(
    BaseModelUUID,
    BaseModelCreatedData,
):
    date = models.DateField()
    bank_account = models.ForeignKey(
        "financial.BankAccount",
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    category = models.ForeignKey(
        "financial.Category",
        on_delete=models.CASCADE,
        related_name="transactions",
        null=True,
        blank=True,
    )
    transaction_type = models.CharField(
        max_length=30,
        choices=TransactionType.choices,
        default=TransactionType.INCOME,
    )
    description = models.TextField()
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
