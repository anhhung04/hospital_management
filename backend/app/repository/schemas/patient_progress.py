from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class PatientProgress(Base):
    __tablename__ = 'patient_progresses'

    medical_record_id = Column(Integer, ForeignKey('patient.medical_record_id'), primary_key=True, index=True)
    progress_date = Column(Date)
    progress = Column(String)
    lead_doctor_id = Column(Integer, ForeignKey('employees.employee_id'))
    treatment_schedule = Column(String)
    treatment_type = Column(String)
    patient_condition = Column(String)
    prescription_id = Column(Integer, ForeignKey('prescription.medID'))
    patient = relationship("Patient", back_populates="patient_progresses", uselist=False)
    employees = relationship("Employee", back_populates="patient_progresses", uselist=False)
    prescription = relationship("Prescription", back_populates="patient_progresses")