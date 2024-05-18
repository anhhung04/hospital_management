from unittest import TestCase
from tests import(
    override_get_db, 
    insert_user, 
    gen_password, 
    gen_username, 
    insert_patient, 
    insert_employee
)
from util.crypto import PasswordContext
from repository.schemas.user import User
from repository.schemas.patient import Patient
from repository.schemas.employees import Employee

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
        self.assertTrue(u_n_db.address == u.address)
        
    def test_insert_patient(self):
        db = next(override_get_db())
        password = gen_password()
        u = insert_user(db, gen_username(), password, 'PATIENT')
        patient = insert_patient(db, u.id)
        patient_n_db = db.query(Patient).filter(Patient.user_id == patient.user_id).first()
        self.assertEqual(patient_n_db.user_id, patient.user_id)
        self.assertEqual(patient_n_db.personal_info, u)

    def test_insert_employee(self):
        db = next(override_get_db())
        password = gen_password()
        u = insert_user(db, gen_username(), password, 'EMPLOYEE')
        employee = insert_employee(db, u.id)
        employee_n_db = db.query(Employee).filter(Employee.user_id == employee.user_id).first()
        self.assertEqual(employee_n_db.user_id, employee.user_id)
        self.assertEqual(employee_n_db.personal_info, u)