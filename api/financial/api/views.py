from rest_framework import viewsets
from ..models import (
    Bank,
    BankAccount,
    Category,
    Transaction,
)
from .serializers import (
    BankSerializer,
    BankAccountSerializer,
    CategorySerializer,
    TransactionSerializer,
)


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
