from unittest import TestCase
from tests import override_get_db, insert_employee_full
from repository.schemas.employees import Employee, FixedSchedule, OvertimeSchedule, EmployeeType, EducateLevel, EmployeeStatus, Frequency, fixed_schedule_of_employee, overtime_schedule_of_employee, ScheduleStatus
from datetime import date, time

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

        # Test FixedSchedule
        fs = FixedSchedule(day="Monday", begin_time=time(9, 0), end_time=time(17, 0), begin_date=date(2022, 1, 1), end_date=date(2022, 12, 31), frequency=Frequency.DAILY)
        db.add(fs)
        db.commit()
        fs_n_db = db.query(FixedSchedule).filter(FixedSchedule.id == fs.id).first()
        self.assertTrue(fs_n_db is not None)
        self.assertTrue(fs_n_db.day == fs.day)
        self.assertTrue(fs_n_db.begin_time == fs.begin_time)
        self.assertTrue(fs_n_db.end_time == fs.end_time)
        self.assertTrue(fs_n_db.begin_date == fs.begin_date)
        self.assertTrue(fs_n_db.end_date == fs.end_date)
        self.assertTrue(fs_n_db.frequency == fs.frequency)

        # Test OvertimeSchedule
        os = OvertimeSchedule(date=date(2022, 1, 1), begin_time=time(17, 0), end_time=time(19, 0))
        db.add(os)
        db.commit()
        os_n_db = db.query(OvertimeSchedule).filter(OvertimeSchedule.id == os.id).first()
        self.assertTrue(os_n_db is not None)
        self.assertTrue(os_n_db.date == os.date)
        self.assertTrue(os_n_db.begin_time == os.begin_time)
        self.assertTrue(os_n_db.end_time == os.end_time)

        # Test fixed_schedule_of_employee
        db.execute(fixed_schedule_of_employee.insert().values(employee_id=e.user_id, schedule_id=fs.id, status=ScheduleStatus.ACTIVE))
        db.commit()
        fs_link = db.query(fixed_schedule_of_employee).filter(fixed_schedule_of_employee.c.schedule_id == fs.id).first()
        self.assertTrue(fs_link is not None)
        self.assertTrue(fs_link.employee_id == e.user_id)
        self.assertTrue(fs_link.status == ScheduleStatus.ACTIVE)

        # Test overtime_schedule_of_employee
        db.execute(overtime_schedule_of_employee.insert().values(employee_id=e.user_id, schedule_id=fs.id, status=ScheduleStatus.ACTIVE))
        db.commit()
        os_link = db.query(overtime_schedule_of_employee).filter(overtime_schedule_of_employee.c.schedule_id == os.id).first()
        self.assertTrue(os_link is not None)
        self.assertTrue(os_link.employee_id == e.user_id)
        self.assertTrue(os_link.status == ScheduleStatus.ACTIVE)


