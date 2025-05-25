from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdminChangeForm(UserChangeForm):
    """
    Custom form for editing existing User instances in the Django admin.
    It inherits from Django's built-in UserChangeForm.
    """

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "birth_date",
            "cpf",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "street",
            "number",
            "complement",
            "neighborhood",
            "city",
            "state",
            "zip_code",
        )


class UserAdminCreationForm(UserCreationForm):
    """
    Custom form for creating new User instances in the Django admin.
    It inherits from Django's built-in UserCreationForm.
    """

    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_("Password confirmation"),
        label_suffix=_(" (again)"),
        widget=forms.PasswordInput,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "birth_date",
            "cpf",
            "is_active",
            "is_staff",
            "is_superuser",
            "street",
            "number",
            "complement",
            "neighborhood",
            "city",
            "state",
            "zip_code",
        )

    def clean_password2(self):
        """
        Custom cleaning method for the password2 field.
        This method explicitly checks if the 'password1' and 'password2' fields match.
        If they don't, it raises a ValidationError.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("The two password fields didn't match."))
        return password2

    def clean(self):
        """
        Overrides the clean method to ensure all form-wide validation is handled.
        Calls the parent's clean method first to get initial cleaned data.
        """
        cleaned_data = super().clean()
        return cleaned_data
