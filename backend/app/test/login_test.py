from unittest import TestCase
import requests

class TestDemo(TestCase):
    def test_login(self):
        response = requests.post("/api/auth/login", json={"username": "test", "password": "test"})
        assert response.status_code == 200
