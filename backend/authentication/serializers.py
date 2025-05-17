from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("cpf", "name", "email", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["cpf"] = user.cpf
        return token


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate_refresh(self, value):
        try:
            self.token = self.get_validated_token(value)
        except Exception:
            raise serializers.ValidationError("Invalid token")
        return value

    def save(self, **kwargs):
        token = RefreshToken(self.validated_data["refresh"])
        token.blacklist()
