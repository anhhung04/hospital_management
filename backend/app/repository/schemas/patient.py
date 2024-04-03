from sqlalchemy import String, Integer, ForeignKey, Float, DateTime, func, Date
from sqlalchemy.orm import mapped_column, Mapped, relationship
from repository.schemas import Base, ObjectID
from typing import List


class Patient(Base):
    __tablename__ = 'patients'
    user_id = mapped_column(ObjectID, ForeignKey('users.id'), primary_key=True)
    medical_record: Mapped["MedicalRecord"] = relationship(back_populates="patient")
    personal_info = relationship("User", primaryjoin="Patient.user_id == User.id", uselist=False)

class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = mapped_column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    created_at = mapped_column(DateTime, default=func.now())
    weight = mapped_column(Float)
    height = mapped_column(Float)
    note = mapped_column(String)
    current_treatment = mapped_column(String)
    drug_allergies = mapped_column(String)
    food_allergies = mapped_column(String)
    medical_history = mapped_column(String)
    patient_id = mapped_column(ForeignKey('patients.user_id'))
    patient: Mapped["Patient"] = relationship(
        "Patient", back_populates="medical_record")
    progress: Mapped[List["PatientProgress"]] = relationship(
        back_populates='medical_record')


class PatientProgress(Base):
    __tablename__ = 'patient_progresses'

    id = mapped_column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    created_at = mapped_column(DateTime, default=func.now())
    treatment_schedule = mapped_column(String)
    treatment_type = mapped_column(String)
    patient_condition = mapped_column(String)
    patient_id = mapped_column(ForeignKey('patients.user_id'))
    patient: Mapped["Patient"] = relationship(
        primaryjoin="PatientProgress.patient_id == Patient.user_id"
    )
    medical_record_id = mapped_column(ForeignKey('medical_records.id'))
    medical_record: Mapped["MedicalRecord"] = relationship(back_populates="progress")
