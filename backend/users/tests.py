from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User, PhoneNumber


class UserTestCase(APITestCase):
    def setUp(self):
        # URL for list/create
        self.list_url = reverse("user-list")

        self.user = User.objects.create_user(
            cpf="12345678900",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            password="john_password",
            birth_date="1990-01-01",
            street="Main St",
            number="123",
            complement="",
            neighborhood="Downtown",
            city="Sample City",
            state="SC",
            zip_code="12345-678",
        )
        PhoneNumber.objects.create(user=self.user, number="+5511988887777")

        # Helper for detail URL
        self.detail_url = lambda cpf: reverse("user-detail", kwargs={"pk": cpf})

        # For user creation/update
        self.user_data = {
            "cpf": "99911122233",
            "first_name": "Alice",
            "last_name": "Smith",
            "birth_date": "1985-05-05",
            "email": "alice@example.com",
            "password": "alice_pass",
            "street": "1st Ave",
            "number": "42",
            "complement": "Apt 2",
            "neighborhood": "Central",
            "city": "Metropolis",
            "state": "MT",
            "zip_code": "00000-000",
            "phone_numbers": [{"number": "+5511990001111"}],
        }

    def test_create_user(self):
        resp = self.client.post(self.list_url, self.user_data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

        new = User.objects.get(cpf=self.user_data["cpf"])
        self.assertEqual(new.email, self.user_data["email"])
        self.assertTrue(new.check_password(self.user_data["password"]))

    def test_create_existing_user_fails(self):
        # CPF is primary key
        new = self.user_data.copy()
        new["cpf"] = self.user.cpf

        resp = self.client.post(self.list_url, new, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

        # Email is unique
        new["cpf"] = self.user_data["cpf"]
        new["email"] = self.user.email

        resp = self.client.post(self.list_url, new, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_list_requires_auth(self):
        # Unauthenticated
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticated
        self.client.force_authenticate(self.user)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        cpfs = [u["cpf"] for u in resp.data]
        self.assertIn(self.user.cpf, cpfs)

    def test_retrieve_requires_auth(self):
        # Unauthenticated
        resp = self.client.get(self.detail_url(self.user.cpf))
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticated
        self.client.force_authenticate(self.user)
        resp = self.client.get(self.detail_url(self.user.cpf))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["email"], self.user.email)

    def test_update_user(self):
        self.client.force_authenticate(self.user)
        updated = self.user_data.copy()
        updated["cpf"] = self.user.cpf
        updated["first_name"] = "Alice"
        updated["phone_numbers"] = [{"number": "+5511990002222"}]

        resp = self.client.put(self.detail_url(self.user.cpf), updated, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Alice")
        self.assertEqual(self.user.phone_numbers.count(), 1)

    def test_update_empty_phone_numbers_fails(self):
        self.client.force_authenticate(self.user)
        bad = self.user_data.copy()
        bad["cpf"] = self.user.cpf
        bad["phone_numbers"] = []
        resp = self.client.put(self.detail_url(self.user.cpf), bad, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_allows_missing_phone_numbers(self):
        self.client.force_authenticate(self.user)
        resp = self.client.patch(
            self.detail_url(self.user.cpf), {"first_name": "Johnny"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Johnny")

    def test_delete_user(self):
        self.client.force_authenticate(self.user)
        resp = self.client.delete(self.detail_url(self.user.cpf))
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(cpf=self.user.cpf).exists())
