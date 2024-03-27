from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum
from enum import Enum
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from repository.schemas import Base

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
    medical_warehouse_management = relationship("MedicalWarehouseManagement", back_populates="employees")
    taking_care = relationship("TakingCare", back_populates="employees")
    patient_progress = relationship("PatientProgress", back_populates="employees", uselist=False)
    schedule = relationship("Schedule", back_populates="employees", uselist=False) 