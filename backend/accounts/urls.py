from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, CurrentAccountViewSet, SavingsAccountViewSet

router = DefaultRouter()
router.register(r"accounts", AccountViewSet)
router.register(r"current-accounts", CurrentAccountViewSet)
router.register(r"savings-accounts", SavingsAccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
