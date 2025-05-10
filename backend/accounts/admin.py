from django.contrib import admin
from .models import Account, CurrentAccount, SavingsAccount


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "balance"]


@admin.register(CurrentAccount)
class CurrentAccountAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "balance", "overdraft_limit", "monthly_income"]


@admin.register(SavingsAccount)
class SavingsAccountAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "balance", "interest_rate", "anniversary_date"]
