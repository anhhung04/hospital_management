from enum import Enum


class UserRole:
    PATIENT = 'PATIENT'
    EMPLOYEE = 'EMPLOYEE'
    ADMIN = 'ADMIN'


class EmployeeType(Enum):
    DOCTOR = 'DOCTOR'
    NURSE = 'NURSE'
    MANAGER = 'MANAGER'
    OTHER = 'OTHER'
