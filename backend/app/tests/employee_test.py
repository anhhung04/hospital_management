from unittest import TestCase
from tests import override_get_db, insert_employee_full
from repository.schemas.employees import Employee, EmployeeType, EducateLevel, EmployeeStatus
from datetime import date

class EmployeeTest(TestCase):
    def test_insert_employee(self):
        db = next(override_get_db())
        user_id = "123"
        employee_type = EmployeeType.DOCTOR
        education_level = EducateLevel.BACHELOR
        begin_date = date(2022, 1, 1)
        end_date = date(2022, 12, 31)
        faculty = "Engineering"
        status = EmployeeStatus.ACTIVE
        e = insert_employee_full(db, user_id, employee_type, education_level, begin_date, end_date, faculty, status)
        e_n_db = db.query(Employee).filter(Employee.user_id == e.user_id).first()
        self.assertTrue(e_n_db is not None)
        self.assertTrue(e_n_db.user_id == e.user_id)
        self.assertTrue(e_n_db.employee_type == e.employee_type)
        self.assertTrue(e_n_db.education_level == e.education_level)
        self.assertTrue(e_n_db.begin_date == e.begin_date)
        self.assertTrue(e_n_db.end_date == e.end_date)
        self.assertTrue(e_n_db.faculty == e.faculty)
        self.assertTrue(e_n_db.status == e.status)


