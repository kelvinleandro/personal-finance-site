from django.contrib import admin
from .models import Account, CurrentAccount, SavingsAccount, Goal


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "balance"]
    search_fields = ("user__email",)


@admin.register(CurrentAccount)
class CurrentAccountAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "balance", "overdraft_limit", "monthly_income"]


@admin.register(SavingsAccount)
class SavingsAccountAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "balance", "interest_rate", "anniversary_date"]


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ["name", "account", "target_amount", "current_amount", "deadline"]
    search_fields = ("name",)
