from unittest import TestCase
from test import override_get_db, gen_password, gen_username, client
from util.crypto import hash_password
from uuid import uuid4
from repository.schemas.user import User

class TestDemo(TestCase):
    def test_login(self):
        db = next(override_get_db())
        u = gen_username()
        p = gen_password()
        db.add(User(id=str(uuid4()), username=u, password=hash_password(p, u)))
        db.commit()
        db.close()
        res = client.post("/api/auth/login",
                          json={"username": u, "password": p})
        self.assertEqual(res.status_code, 200)
        self.assertTrue("access_token" in res.json()['data'])

    def test_login_fail(self):
        res = client.post("/api/auth/login",
                          json={"username": gen_username(), "password": gen_password()})
        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.json()['message'],
                         "Incorrect username or password")
