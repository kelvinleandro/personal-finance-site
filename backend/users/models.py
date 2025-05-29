from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, cpf, email, password=None, **extra_fields):
        if not cpf:
            raise ValueError("CPF is required")
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(cpf=cpf, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(cpf, email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    cpf = models.CharField(max_length=14, unique=True, primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField(null=True)
    email = models.EmailField(unique=True)

    tel1 = models.CharField(max_length=20, blank=True)
    tel2 = models.CharField(max_length=20, blank=True)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Address
    street = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=20, blank=True)
    neighborhood = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2, help_text="E.g., SP, RJ, MG")
    zip_code = models.CharField(max_length=10)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["cpf"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.cpf})"
