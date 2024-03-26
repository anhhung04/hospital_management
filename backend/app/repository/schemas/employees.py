from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Employees(Base):
    __tablename__ = 'Employees'

    employee_id = Column(Integer, primary_key=True, index=True)
    ssn = Column(Integer, ForeignKey('personal_infos.ssn'), unique=True)
    position = Column(String)
    employee_type = Column(Enum)
    education_level = Column(Enum)
    cert1 = Column(String)
    cert2 = Column(String)
    cert3 = Column(String)
    begin = Column(Date)
    end = Column(Date)
    person = relationship("Person", back_populates="employee", uselist=False)
    medical_warehouse_management = relationship("MedicalWarehouseManagement", back_populates="employees")
    taking_care = relationship("TakingCare", back_populates="employees")
    patient_progress = relationship("PatientProgress", back_populates="employees", uselist=False)
    schedule = relationship("Schedule", back_populates="employees", uselist=False) 