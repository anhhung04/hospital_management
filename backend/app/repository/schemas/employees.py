from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy import Enum as DBEnum
from sqlalchemy.orm import mapped_column, relationship
from repository.schemas import Base, ObjectID
from enum import Enum
from permissions.user import EmployeeType

class Level(Enum):
    BACHELOR = 'bachelor'
    MASTER = 'master'
    DOCTOR = 'doctor'
    UNDERGRADUATE = 'undergraduate'
    UNKNOWN = 'unknown'

class Employee(Base):
    __tablename__ = 'employees'

    employee_id = mapped_column(ObjectID, ForeignKey('users.id'), primary_key=True, unique=True)
    position = mapped_column(String)
    employee_type = mapped_column(DBEnum(EmployeeType))
    education_level = mapped_column(DBEnum(Level))
    begin = mapped_column(Date)
    end = mapped_column(Date)
    faculty = mapped_column(String)
    personal_info = relationship("User", back_populates="employees", uselist=False)