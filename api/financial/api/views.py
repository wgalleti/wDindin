from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.mixins.views import BaseViewSet
from ..models import (
    Bank,
    BankAccount,
    Category,
    Transaction,
)
from .serializers import (
    BankSerializerV1,
    BankAccountSerializerV1,
    CategorySerializerV1,
    TransactionSerializerV1,
)


class BankViewSetV1(BaseViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializerV1


class BankAccountViewSetV1(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializerV1

    @action(methods=["GET"], detail=False)
    def types(self, request):
        data = [
            {"id": key, "name": value}
            for key, value in BankAccount.BankAccountType.choices
        ]
        return Response(data)


class CategoryViewSetV1(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerV1


class TransactionViewSetV1(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializerV1
