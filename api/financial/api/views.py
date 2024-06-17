from rest_framework import viewsets
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


class BankViewSetV1(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializerV1


class BankAccountViewSetV1(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializerV1


class CategoryViewSetV1(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerV1


class TransactionViewSetV1(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializerV1
