from rest_framework import viewsets
from .models import Card, CreditCard, DebitCard
from .serializers import CardSerializer, CreditCardSerializer, DebitCardSerializer


class CardViewSet(viewsets.ModelViewSet):
    # queryset = Card.objects.all()
    queryset = Card.objects.select_related("account")
    serializer_class = CardSerializer


class CreditCardViewSet(viewsets.ModelViewSet):
    # queryset = CreditCard.objects.all()
    queryset = CreditCard.objects.select_related("account")
    serializer_class = CreditCardSerializer


class DebitCardViewSet(viewsets.ModelViewSet):
    # queryset = DebitCard.objects.all()
    queryset = DebitCard.objects.select_related("account")
    serializer_class = DebitCardSerializer
