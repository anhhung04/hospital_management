from unittest import TestCase
from test import override_get_db, client, gen_username, gen_password, create_user


def login(db):
    user, raw_password = create_user()
    db.add(user)
    db.commit()
    res = client.post(
        "/api/auth/login", json={"username": user.username, "password": raw_password})
    return res, user

class TestDemo(TestCase):
    def test_login(self):
        db = next(override_get_db())
        res, _ = login(db)
        self.assertEqual(res.status_code, 200)
        self.assertTrue("access_token" in res.json()['data'])

    def test_login_fail(self):
        res = client.post("/api/auth/login",
                          json={"username": gen_username(), "password": gen_password()})
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.json()['message'], "Nonexistent user")

    def test_verify_token(self):
        res, user = login(next(override_get_db()))
        res = client.post(
            "/api/auth/verify", json={"access_token": res.json()['data']['access_token']})
        res_json = res.json()
        self.assertTrue(res.status_code, 200)
        self.assertIn("data", res_json)
        self.assertIn("is_login", res_json['data'])
        self.assertIn("username", res_json['data'])
        self.assertIn("user_id", res_json['data'])
        self.assertEqual(
            str(user.id), res_json['data']['user_id'], 'invalid id')
        self.assertEqual(
            user.username, res_json['data']['username'], 'invalid username')
