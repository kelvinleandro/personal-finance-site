from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, PhoneNumber

# Register your models here.


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1  # Number of empty phone number rows to show by default


class UserAdmin(BaseUserAdmin):
    list_display = (
        "cpf",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "birth_date",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("cpf", "email", "first_name", "last_name")
    ordering = ("last_name", "first_name", "cpf")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "birth_date", "cpf")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login",)}),
    )

    inlines = [PhoneNumberInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
