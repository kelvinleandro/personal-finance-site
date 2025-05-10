from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CardViewSet, CreditCardViewSet, DebitCardViewSet

router = DefaultRouter()
router.register(r"cards", CardViewSet)
router.register(r"credit-cards", CreditCardViewSet)
router.register(r"debit-cards", DebitCardViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
