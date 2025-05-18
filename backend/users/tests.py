from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User


class UserTestCase(APITestCase):
    def test_create_user(self):
        url = reverse("user-list")
        data = {
            "cpf": "12345678900",
            "name": "John Doe",
            "birth_date": "1990-01-01",
            "email": "john@example.com",
            "password": "john_password",
            "is_active": True,
            "is_staff": False,
            "street": "Main St",
            "number": "123",
            "complement": "",
            "neighborhood": "Downtown",
            "city": "Sample City",
            "state": "SC",
            "zip_code": "12345-678",
            "phone_numbers": [{"number": "+5511999999999"}],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, data["email"])
