from django.db import models
from accounts.models import Account


class Card(models.Model):
    number = models.CharField(max_length=20, unique=True, primary_key=True)
    expiring_date = models.DateField()
    security_code = models.CharField(max_length=4)
    account = models.ForeignKey(Account, related_name="cards", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    def __str__(self):
        return f"{self.__class__.__name__} #{self.number}"


class CreditCard(Card):
    current_balance = models.DecimalField(max_digits=12, decimal_places=2)
    invoice_due_date = models.DateField()
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2)


class DebitCard(Card):
    current_balance = models.DecimalField(max_digits=12, decimal_places=2)
    daily_limit = models.DecimalField(max_digits=12, decimal_places=2)
