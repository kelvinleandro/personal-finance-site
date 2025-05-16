from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AccountViewSet,
    CurrentAccountViewSet,
    SavingsAccountViewSet,
    GoalViewSet,
)

router = DefaultRouter()
router.register(r"accounts", AccountViewSet)
router.register(r"current-accounts", CurrentAccountViewSet)
router.register(r"savings-accounts", SavingsAccountViewSet)
router.register(r"goals", GoalViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
