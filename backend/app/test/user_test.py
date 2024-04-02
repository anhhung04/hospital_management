from unittest import TestCase
from test import override_get_db, insert_user
from util.crypto import hash_password
from repository.schemas.user import User

class UserTest(TestCase):
    def test_insert_user(self):
        db = next(override_get_db())
        u = insert_user(db)
        u_n_db = db.query(User).filter(User.id == u.id).first()
        self.assertTrue(u_n_db is not None)
        self.assertTrue(u_n_db.id is not None)
        self.assertTrue(u_n_db.username == u.username)
        self.assertTrue(u_n_db.password == u.password)
        self.assertTrue(u_n_db.phone_number == u.phone_number)
        self.assertTrue(u_n_db.user_type == u.user_type)
        self.assertTrue(u_n_db.ssn == u.ssn)
        self.assertTrue(u_n_db.first_name == u.first_name)
        self.assertTrue(u_n_db.last_name == u.last_name)
        self.assertTrue(u_n_db.nation == u.nation)
        self.assertTrue(u_n_db.district == u.district)
        self.assertTrue(u_n_db.ward == u.ward)
        self.assertTrue(u_n_db.address == u.address)