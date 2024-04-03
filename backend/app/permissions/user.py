from enum import Enum


class UserRole:
    PATIENT = 'patient'
    EMPLOYEE = 'employee'
    ADMIN = 'admin'

class EmployeeType(Enum):
    DOCTOR = 'doctor'
    NURSE = 'nurse'
    MANAGER = 'manager'
