from sqlalchemy import (
    String, Integer, ForeignKey, Float, DateTime, func,
    Enum as DBEnum
)
from sqlalchemy.orm import mapped_column, Mapped, relationship
from repository.schemas import Base, ObjectID
from typing import List
from enum import Enum

class ProgressType(Enum):
    SCHEDULING = 'SCHEDULING'
    PROCESSING = 'PROCESSING'
    FINISHED = 'FINISHED'

class Patient(Base):
    __tablename__ = 'patients'
    user_id = mapped_column(ObjectID, ForeignKey('users.id'), primary_key=True)
    medical_record_id = mapped_column(ForeignKey('medical_records.id'))
    medical_record: Mapped["MedicalRecord"] = relationship(back_populates="patient")
    personal_info = relationship("User", primaryjoin="Patient.user_id == User.id", uselist=False)

    __table_args__ = {"extend_existing": True}

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
    patient: Mapped["Patient"] = relationship(
        "Patient", back_populates="medical_record")
    progress: Mapped[List["PatientProgress"]] = relationship(
        back_populates='medical_record')

    __table_args__ = {"extend_existing": True}


class EmployeeHandlePatient(Base):
    __tablename__ = 'in_charge_of_patients'
    employee_id = mapped_column(ForeignKey(
        'employees.user_id'), primary_key=True)
    progress_id = mapped_column(ForeignKey(
        'patient_progresses.id'), primary_key=True)
    employee = relationship(
        "Employee",
        primaryjoin="EmployeeHandlePatient.employee_id == Employee.user_id"
    )
    progress = relationship(
        "PatientProgress",
        primaryjoin="PatientProgress.id == EmployeeHandlePatient.progress_id"
    )
    action = mapped_column(String, default='')


class PatientProgress(Base):
    __tablename__ = 'patient_progresses'

    id = mapped_column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    created_at = mapped_column(DateTime, default=func.now())
    start_treatment = mapped_column(DateTime, default=func.now())
    end_treatment = mapped_column(DateTime)
    patient_condition = mapped_column(String)
    patient_id = mapped_column(ForeignKey('patients.user_id'))
    status = mapped_column(DBEnum(ProgressType),
                           default=ProgressType.SCHEDULING)
    medical_record_id = mapped_column(ForeignKey('medical_records.id'))
    medical_record: Mapped["MedicalRecord"] = relationship(back_populates="progress")
    lead_employee: Mapped[List["EmployeeHandlePatient"]] = relationship(
        "EmployeeHandlePatient",
        primaryjoin="PatientProgress.id == EmployeeHandlePatient.progress_id"
    )

    __table_args__ = {"extend_existing": True}
