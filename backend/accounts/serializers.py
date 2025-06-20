from rest_framework import serializers
from .models import Account, CurrentAccount, SavingsAccount, Goal


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class CurrentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentAccount
        fields = "__all__"


class SavingsAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsAccount
        fields = "__all__"


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"
