from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from repository.schemas import Base, ObjectID
from typing import List


class Patient(Base):
    __tablename__ = 'patients'
    user_id = mapped_column(ObjectID, ForeignKey('users.id'), primary_key=True)
    weight = mapped_column(Integer)
    height = mapped_column(Integer)
    note = mapped_column(String)
    medical_record: Mapped["MedicalRecord"] = relationship(back_populates="patient")
    personal_info = relationship("User", primaryjoin="Patient.user_id == User.id", uselist=False)

class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = mapped_column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    patient_id = mapped_column(ForeignKey('patients.user_id'))
    patient: Mapped["Patient"] = relationship(
        "Patient", back_populates="medical_record")
    progress: Mapped[List["PatientProgress"]] = relationship(
        back_populates='medical_record')


class PatientProgress(Base):
    __tablename__ = 'patient_progresses'

    id = mapped_column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    date = mapped_column(Date)
    treatment_schedule = mapped_column(String)
    treatment_type = mapped_column(String)
    patient_condition = mapped_column(String)
    patient_id = mapped_column(ForeignKey('patients.user_id'))
    patient: Mapped["Patient"] = relationship(
        primaryjoin="PatientProgress.patient_id == Patient.user_id"
    )
    medical_record_id = mapped_column(ForeignKey('medical_records.id'))
    medical_record: Mapped["MedicalRecord"] = relationship(back_populates="progress")
