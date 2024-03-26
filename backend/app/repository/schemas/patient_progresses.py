from sqlalchemy import Table, String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class PatientProgress(Base):
    __tablename__ = 'patient_progresses'

    progress_id = mapped_column(Integer, primary_key=True, index=True)
    patient_id = mapped_column(Integer, ForeignKey('patients.medID'), index=True)
    medical_record_id = mapped_column(Integer, ForeignKey('patients.medical_record_id'))
    progress_date = mapped_column(Date)
    progress = mapped_column(String)
    lead_doctor_id = mapped_column(Integer, ForeignKey('employees.employee_id'))
    treatment_schedule = mapped_column(String)
    treatment_type = mapped_column(String)
    patient_condition = mapped_column(String)
    prescription_id = mapped_column(Integer, ForeignKey('prescriptions.prescription_id'))
    patient = relationship("Patient", back_populates="patient_progresses", uselist=False)
    employee = relationship("Employee", back_populates="patient_progresses", uselist=False)
    prescription = relationship("Prescription", back_populates="patient_progresses")