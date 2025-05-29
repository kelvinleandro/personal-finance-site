from django.db import transaction
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "cpf",
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "password",
            "street",
            "number",
            "complement",
            "neighborhood",
            "city",
            "state",
            "zip_code",
            "tel1",
            "tel2",
        ]

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        return instance
