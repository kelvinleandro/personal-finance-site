from django.db import models
from users.models import User


class Account(models.Model):
    user = models.ForeignKey(User, related_name="accounts", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return f"{self.__class__.__name__} #{self.pk} - {self.user.email}"


class CurrentAccount(Account):
    overdraft_limit = models.DecimalField(max_digits=12, decimal_places=2)
    monthly_income = models.DecimalField(max_digits=12, decimal_places=2)


class SavingsAccount(Account):
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    anniversary_date = models.DateField()


class Goal(models.Model):
    account = models.ForeignKey(Account, related_name="goals", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deadline = models.DateField()

    class Meta:
        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def __str__(self):
        return f"{self.name} - {self.account}"
