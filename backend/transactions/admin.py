from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "transaction_type", "value", "date", "account")
    list_filter = ("transaction_type", "date", "category", "goal")
    search_fields = ("name",)
    autocomplete_fields = (
        "account",
        "category",
        "goal",
        "credit_card",
        "linked_transaction",
    )
