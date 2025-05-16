from django.db import models
from accounts.models import Account, Goal
from cards.models import Card
from categories.models import Category


class Transaction(models.Model):
    INCOME = "income"
    EXPENSE = "expense"

    TRANSACTION_TYPES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    ]

    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    installments = models.BinaryField(default=1)
    date = models.DateField()

    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )
    goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, null=True, blank=True)
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"{self.name} - {self.transaction_type} - {self.value}"
