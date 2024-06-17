from rest_framework import serializers

from core.mixins.serializers import BaseModelCreatedSerializer
from ..models import (
    Bank,
    BankAccount,
    Category,
    Transaction,
)


class BankSerializer(BaseModelCreatedSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class BankAccountSerializer(BaseModelCreatedSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"


class CategorySerializer(BaseModelCreatedSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TransactionSerializer(BaseModelCreatedSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
