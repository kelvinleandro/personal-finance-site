from rest_framework import viewsets
from .models import Account, CurrentAccount, SavingsAccount, Goal
from .serializers import (
    AccountSerializer,
    CurrentAccountSerializer,
    SavingsAccountSerializer,
    GoalSerializer,
)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CurrentAccountViewSet(viewsets.ModelViewSet):
    queryset = CurrentAccount.objects.select_related("user")
    serializer_class = CurrentAccountSerializer


class SavingsAccountViewSet(viewsets.ModelViewSet):
    queryset = SavingsAccount.objects.select_related("user")
    serializer_class = SavingsAccountSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
