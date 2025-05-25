from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User, PhoneNumber


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 0  # Number of empty phone number rows to show by default


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

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
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "birth_date", "cpf")},
        ),
        (
            _("Address"),
            {
                "fields": (
                    "street",
                    "number",
                    "complement",
                    "neighborhood",
                    "city",
                    "state",
                    "zip_code",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login",)},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "birth_date", "cpf")},
        ),
        (
            _("Address info"),
            {
                "fields": (
                    "street",
                    "number",
                    "complement",
                    "neighborhood",
                    "city",
                    "state",
                    "zip_code",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    # "groups",
                    # "user_permissions",
                )
            },
        ),
    )

    inlines = [PhoneNumberInline]


admin.site.register(User, UserAdmin)
