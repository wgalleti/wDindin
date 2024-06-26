from cryptography.fernet import Fernet
from rest_framework import serializers

from config import settings
from core.mixins.serializers import BaseModelCreatedSerializer
from ..models import (
    Bank,
    BankAccount,
    Category,
    Transaction,
    CreditCard,
    TransactionType,
)


class BankSerializerV1(BaseModelCreatedSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class BankAccountSerializerV1(BaseModelCreatedSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"


class CreditCardSerializerV1(BaseModelCreatedSerializer):
    expiration_date = serializers.CharField(
        max_length=5,
    )
    balance = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = CreditCard
        fields = [
            "id",
            "expiration_date",
            "created_at",
            "updated_at",
            "created_by",
            "name",
            "flag",
            "final_number",
            "limit",
            "bank",
            "balance",
        ]

    def get_expiration_date(self, obj: CreditCard):
        return obj.expiration_date

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        expiration_date = internal_value.get("expiration_date")
        if expiration_date:
            f = Fernet(settings.CRYPTOGRAPHY_KEY)
            encrypted_date = f.encrypt(expiration_date.encode("utf-8"))
            internal_value["_expiration_date"] = encrypted_date
        return internal_value

    def create(self, validated_data):
        validated_data.pop("expiration_date")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("expiration_date", None)
        return super().update(instance, validated_data)

    def validate_final_number(self, value):
        if not value.isdigit() or len(value) != 4:
            raise serializers.ValidationError(
                "Last four digits must be exactly 4 numbers."
            )
        return value

    def validate_expiration_date(self, value):
        if len(value) != 5 or value[2] != "/":
            raise serializers.ValidationError(
                "Expiration date must be in MM/YY format."
            )
        return value


class CategorySerializerV1(BaseModelCreatedSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TransactionSerializerV1(BaseModelCreatedSerializer):

    def _validate_credit_card(self, data):
        value = data.get("value", 0)
        credit_card: CreditCard = data.get("credit_card", None)

        if not credit_card:
            return

        # Validate category Expense
        category: Category = data.get("category")
        if category.transaction_type == TransactionType.INCOME:
            raise serializers.ValidationError("Credit Card has not receive income")

        # Validate limit
        available_value = credit_card.balance
        total = available_value - value
        if total < 0:
            raise serializers.ValidationError("Credit Card has not limit")

    def validate(self, data):
        self._validate_credit_card(data)

        return data

    class Meta:
        model = Transaction
        fields = "__all__"
