# src/tradely/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import TradingAccount


class TradingAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.test_account = TradingAccount.objects.create(
            user=self.user,
            platform_type="MT5",
            account_number="123456",
            password="testpass",
            server="DemoServer",
        )

    def test_mt_account_authentication(self):
        url = reverse("mt-auth")
        data = {
            "platform_type": "MT5",
            "account_number": "123456",
            "password": "testpass",
            "server": "DemoServer",
        }
        response = self.client.post(url, data, format="json")
        if response.status_code != status.HTTP_201_CREATED:
            print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_trade_list_retrieval(self):
        url = reverse("trade-list", args=[self.test_account.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("trades", response.data)
