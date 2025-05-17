from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AccountViewSet,
    CurrentAccountViewSet,
    SavingsAccountViewSet,
    GoalViewSet,
)

router = DefaultRouter()
router.register(r"", AccountViewSet, basename="account")
router.register(r"current-accounts", CurrentAccountViewSet, basename="currentaccount")
router.register(r"savings-accounts", SavingsAccountViewSet, basename="savingsaccount")
router.register(r"goals", GoalViewSet, basename="goal")

urlpatterns = [
    path("", include(router.urls)),
]
