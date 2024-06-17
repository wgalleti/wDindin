from django.contrib import admin

from core.mixins.admin import BaseAdminCreatedMixin
from .models import Bank, BankAccount, Category, Transaction


@admin.register(Bank)
class BankAdmin(BaseAdminCreatedMixin):
    search_fields = [
        "name",
        "code",
    ]
    list_display = (
        "name",
        "code",
    )


@admin.register(BankAccount)
class BankAccountAdmin(BaseAdminCreatedMixin):
    autocomplete_fields = [
        "bank",
    ]
    search_fields = [
        "name",
        "account_type",
    ]
    list_display = [
        "bank",
        "name",
        "initial_balance",
        "account_type",
    ]
    list_filter = [
        "account_type",
        "bank",
    ]


@admin.register(Category)
class CategoryAdmin(BaseAdminCreatedMixin):
    search_fields = ["name"]
    list_display = [
        "name",
        "icon",
        "transaction_type",
    ]
    list_filter = [
        "transaction_type",
    ]


@admin.register(Transaction)
class TransactionAdmin(BaseAdminCreatedMixin):
    autocomplete_fields = [
        "bank_account",
        "category",
    ]
    search_fields = [
        "description",
        "category__name",
        "bank_account__name",
        "bank_account__bank__name",
    ]
    list_display = [
        "date",
        "bank_account",
        "category",
        "description",
        "transaction_type",
        "value",
    ]
    list_filter = [
        "bank_account",
        "category",
        "date",
    ]
