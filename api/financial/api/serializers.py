from core.mixins.serializers import BaseModelCreatedSerializer
from ..models import (
    Bank,
    BankAccount,
    Category,
    Transaction,
)


class BankSerializerV1(BaseModelCreatedSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class BankAccountSerializerV1(BaseModelCreatedSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"


class CategorySerializerV1(BaseModelCreatedSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TransactionSerializerV1(BaseModelCreatedSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
