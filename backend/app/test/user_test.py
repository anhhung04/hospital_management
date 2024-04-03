from unittest import TestCase
from test import override_get_db, insert_user, gen_password, gen_username, insert_patient
from util.crypto import PasswordContext
from repository.schemas.user import User
from repository.schemas.patient import Patient

class UserTest(TestCase):
    def test_insert_user(self):
        db = next(override_get_db())
        password = gen_password()
        u = insert_user(db, gen_username(), password)
        u_n_db = db.query(User).filter(User.id == u.id).first()
        self.assertTrue(u_n_db is not None)
        self.assertTrue(u_n_db.id is not None)
        self.assertTrue(u_n_db.username == u.username)
        self.assertTrue(PasswordContext(password, u.username).verify(u_n_db.password))
        self.assertTrue(u_n_db.phone_number == u.phone_number)
        self.assertTrue(u_n_db.role == u.role)
        self.assertTrue(u_n_db.ssn == u.ssn)
        self.assertTrue(u_n_db.first_name == u.first_name)
        self.assertTrue(u_n_db.last_name == u.last_name)
        self.assertTrue(u_n_db.nation == u.nation)
        self.assertTrue(u_n_db.address == u.address)
        
    def test_insert_patient(self):
        db = next(override_get_db())
        password = gen_password()
        u = insert_user(db, gen_username(), password, 'PATIENT')
        patient = insert_patient(db, u.id)
        patient_n_db = db.query(Patient).filter(Patient.user_id == patient.user_id).first()
        self.assertEqual(patient_n_db.user_id, patient.user_id)
        self.assertEqual(patient_n_db.personal_info, u)