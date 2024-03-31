from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.orm import mapped_column, relationship
from repository.schemas import Base
from enum import Enum

class Role(Enum):
    DOCTOR = 1
    NURSE = 2
    PATIENT = 3
    MANAGER = 4

class Level(Enum):
    BACHELOR = 1
    MASTER = 2
    DOCTOR = 3
    UNDERGRADUATE = 4
    UNKNOWN = 5

class Employee(Base):
    __tablename__ = 'employees'

    employee_id = mapped_column(Integer, primary_key=True, index=True, unique=True)
    user_id = mapped_column(String, ForeignKey('users.id'), unique=True)
    position = mapped_column(String)
    employee_type = mapped_column(SQLAlchemyEnum(Role))
    education_level = mapped_column(SQLAlchemyEnum(Level))
    begin = mapped_column(Date)
    end = mapped_column(Date)
    faculty = mapped_column(String)
    user = relationship("User", back_populates="employees", uselist=False)