from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = (
        "cpf",
        "first_name",
        "last_name",
        "email",
        "tel1",
        "is_active",
        "is_staff",
        "is_superuser",
        "birth_date",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("cpf", "email", "first_name", "last_name", "tel1")
    ordering = ("last_name", "first_name", "cpf")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "birth_date", "cpf")},
        ),
        (
            _("Contact Information"),
            {"fields": ("tel1", "tel2")},
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
            _("Contact Information"),
            {"fields": ("tel1", "tel2")},
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


admin.site.register(User, UserAdmin)
