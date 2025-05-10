from django.contrib import admin
from .models import Card, CreditCard, DebitCard


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["number", "expiring_date", "account"]


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ["number", "credit_limit", "current_balance", "invoice_due_date"]


@admin.register(DebitCard)
class DebitCardAdmin(admin.ModelAdmin):
    list_display = ["number", "daily_limit", "current_balance"]
