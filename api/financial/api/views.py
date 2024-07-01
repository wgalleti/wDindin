from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.mixins.views import BaseViewSet
from ..models import (
    Bank,
    BankAccount,
    Category,
    Transaction,
    TransactionType,
    CreditCard,
)
from .serializers import (
    BankSerializerV1,
    BankAccountSerializerV1,
    CategorySerializerV1,
    TransactionSerializerV1,
    CreditCardSerializerV1,
    TransactionListSerializerV1,
    BankAccountListSerializerV1,
    CreditCardListSerializerV1,
)


class BankViewSetV1(BaseViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializerV1


class BankAccountViewSetV1(BaseViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializerV1
    list_serializer_class = BankAccountListSerializerV1

    @action(methods=["GET"], detail=False)
    def types(self, request):
        data = [
            {
                "id": key,
                "name": value,
            }
            for key, value in BankAccount.BankAccountType.choices
        ]
        return Response(data)


class CreditCardViewSetV1(BaseViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializerV1
    list_serializer_class = CreditCardListSerializerV1

    @action(methods=["GET"], detail=False)
    def flags(self, request):
        data = [
            {
                "id": key,
                "name": value,
            }
            for key, value in CreditCard.CreditCardFlag.choices
        ]
        return Response(data)


class CategoryViewSetV1(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerV1

    @action(methods=["GET"], detail=False)
    def types(self, request):
        data = [
            {
                "id": key,
                "name": value,
            }
            for key, value in TransactionType.choices
        ]
        return Response(data)


class TransactionViewSetV1(BaseViewSet):
    queryset = Transaction.objects.all().order_by("-created_at")
    serializer_class = TransactionSerializerV1
    list_serializer_class = TransactionListSerializerV1
