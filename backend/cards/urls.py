from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CardViewSet, CreditCardViewSet, DebitCardViewSet

router = DefaultRouter()
router.register(r"", CardViewSet, basename="card")
router.register(r"credit-cards", CreditCardViewSet, basename="creditcard")
router.register(r"debit-cards", DebitCardViewSet, basename="debitcard")

urlpatterns = [
    path("", include(router.urls)),
]
