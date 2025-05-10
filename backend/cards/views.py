from rest_framework import viewsets
from .models import Card, CreditCard, DebitCard
from .serializers import CardSerializer, CreditCardSerializer, DebitCardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer


class DebitCardViewSet(viewsets.ModelViewSet):
    queryset = DebitCard.objects.all()
    serializer_class = DebitCardSerializer
