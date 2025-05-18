from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import PhoneNumber

User = get_user_model()


class AuthenticationTestCase(APITestCase):
    def setUp(self):
        # create a test user
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
        self.email = self.user.email
        self.password = "john_password"

        PhoneNumber.objects.create(user=self.user, number="+5511988887777")

        # endpoints
        self.login_url = reverse("auth-login")
        self.refresh_url = reverse("auth-refresh")
        self.logout_url = reverse("auth-logout")

    def _get_tokens(self):
        """Helper: obtain JWT pair for testuser."""
        resp = self.client.post(
            self.login_url,
            {"email": self.email, "password": self.password},
            format="json",
        )
        return resp

    def test_login_success(self):
        resp = self._get_tokens()
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("access", resp.data)
        self.assertIn("refresh", resp.data)

    def test_login_failure(self):
        resp = self.client.post(
            self.login_url,
            {"email": self.email, "password": "wrongpass"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_token_success(self):
        login_resp = self._get_tokens()
        refresh = login_resp.data["refresh"]
        resp = self.client.post(self.refresh_url, {"refresh": refresh}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("access", resp.data)

        self.assertNotEqual(resp.data["access"], login_resp.data["access"])

    def test_refresh_token_failure(self):
        login_resp = self._get_tokens()
        access = login_resp.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

        resp = self.client.post(
            self.refresh_url, {"refresh": "bad_refresh"}, format="json"
        )
        self.assertNotEqual(resp.status_code, status.HTTP_200_OK)

    def test_logout_requires_authentication(self):
        resp = self.client.post(self.logout_url, {"refresh": "whatever"}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_invalid_refresh(self):
        login_resp = self._get_tokens()
        access = login_resp.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

        # post invalid refresh token
        resp = self.client.post(
            self.logout_url, {"refresh": "invalidtoken"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_success_and_blacklist(self):
        # obtain tokens and set auth header
        login_resp = self._get_tokens()
        access = login_resp.data["access"]
        refresh = login_resp.data["refresh"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        # logout
        resp = self.client.post(self.logout_url, {"refresh": refresh}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        # now that refresh is blacklisted, attempting to refresh should fail
        resp2 = self.client.post(self.refresh_url, {"refresh": refresh}, format="json")
        self.assertEqual(resp2.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", resp2.data)
