from rest_framework import serializers
from .models import Card, CreditCard, DebitCard


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = "__all__"


class DebitCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitCard
        fields = "__all__"
