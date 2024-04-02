from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from repository.schemas import Base, ObjectID

class PatientProgress(Base):
    __tablename__ = 'patient_progress'

    progress_id = mapped_column(Integer, primary_key=True, index=True)
    patient_id = mapped_column(ObjectID, ForeignKey('patients.patient_id'), index=True)
    medical_record_id = mapped_column(Integer, ForeignKey('patients.medical_record_id'))
    progress_date = mapped_column(Date)
    lead_doctor_id = mapped_column(ObjectID, ForeignKey('employees.employee_id'))
    nurse_id = mapped_column(ObjectID, ForeignKey('employees.employee_id'))
    treatment_schedule = mapped_column(String)
    treatment_type = mapped_column(String)
    patient_condition = mapped_column(String)
    patient = relationship("Patient", back_populates="patient_progress", uselist=False)
    employee = relationship("Employee", back_populates="patient_progress")
    medical_record = relationship("MedicalRecord", back_populates="progress")

class MedicalRecord(Base):
    __tablename__ = 'medical_record'

    medical_record_id = mapped_column(Integer, primary_key=True, index=True)
    patient_id = mapped_column(ObjectID, ForeignKey('patients.patient_id'), index=True)
    progress_id = mapped_column(Integer, ForeignKey('patient_progress.progress_id'))
    patient = relationship("Patient", back_populates="medical_record", uselist=False)

class Patient(Base):
    __tablename__ = 'patients'

    patient_id = mapped_column(ObjectID, ForeignKey('users.id'), primary_key=True, unique=True, index=True)
    medical_record_id = mapped_column(Integer, index=True, unique=True)
    weight = mapped_column(Integer)
    height = mapped_column(Integer)
    note = mapped_column(String)
    personal_info = relationship("User", back_populates="patients", uselist=False)