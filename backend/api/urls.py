from django.urls import path, include

urlpatterns = [
    path("", include("users.urls")),
    path("", include("accounts.urls")),
    path("", include("cards.urls")),
    path("", include("transactions.urls")),
    path("", include("categories.urls")),
]
