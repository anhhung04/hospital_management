from sqlalchemy import String, Date, ForeignKey
from sqlalchemy import Enum as DBEnum
from sqlalchemy.orm import mapped_column, relationship
from enum import Enum
from permissions.user import EmployeeType
from repository.schemas import Base, ObjectID


class EducateLevel(Enum):
    BACHELOR = 'bachelor'
    MASTER = 'master'
    DOCTOR = 'doctor'
    UNDERGRADUATE = 'undergraduate'
    UNKNOWN = 'unknown'


class EmployeeStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'
    SUSPENDED = 'suspended'
    WIP = 'work in progress'

class Employee(Base):
    __tablename__ = 'employees'

    user_id = mapped_column(ObjectID, ForeignKey(
        'users.id'), primary_key=True, unique=True)
    employee_type = mapped_column(DBEnum(EmployeeType))
    education_level = mapped_column(DBEnum(EducateLevel))
    begin_date = mapped_column(Date)
    end_date = mapped_column(Date)
    faculty = mapped_column(String)
    status = mapped_column(DBEnum(EmployeeStatus))
    personal_info = relationship("User", back_populates="employees", uselist=False)