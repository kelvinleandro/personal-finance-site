from django.db import transaction
from rest_framework import serializers
from .models import User, PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        exclude = ("user",)


class UserSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "cpf",
            "name",
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
            "phone_numbers",
        ]

    def validate_phone_numbers(self, value):
        if not value or len(value) == 0:
            raise serializers.ValidationError("At least one phone number is required.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        phone_numbers_data = validated_data.pop("phone_numbers")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        for phone_data in phone_numbers_data:
            PhoneNumber.objects.create(user=user, **phone_data)

        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        phone_numbers_data = validated_data.pop("phone_numbers", None)
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        if phone_numbers_data is not None:
            if len(phone_numbers_data) == 0:
                raise serializers.ValidationError(
                    "At least one phone number is required."
                )

            instance.phone_numbers.all().delete()
            for phone_data in phone_numbers_data:
                PhoneNumber.objects.create(user=instance, **phone_data)

        return instance
