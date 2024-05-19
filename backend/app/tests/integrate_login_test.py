from tests import TestIntegration


class TestCase(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/auth"

    def test_change_password(self):
        res = self._s.post(self.path('/password/change'), json={
            "old_password": "demo",
            "new_password": "admin"
        })
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()['data']['success'])
        res = self._s.post(self.path('/login'), json={
            "username": "employee1",
            "password": "admin"
        })
        self.assertEqual(res.status_code, 200)
        self.assertTrue("access_token" in res.json()['data'])
        access_token = res.json()['data']['access_token']
        self._access_token = access_token
        self._s.headers.update({
            "Authorization": f"Bearer {access_token}"
        })
        res = self._s.post(self.path('/password/change'), json={
            "old_password": "admin",
            "new_password": "demo"
        })
        self.assertTrue(res.status_code, 200)
