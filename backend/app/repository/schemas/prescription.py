from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Prescription(Base):
    __tablename__ = 'prescriptions'

    medID = Column(Integer, primary_key=True, index=True)
    medical_record_id = Column(Integer, primary_key=True, index=True)
    prescription_date = Column(Date)
    quantity = Column(Integer)
    dosage = Column(String)
    usage = Column(String)
    note = Column(String)
    patient_progress = relationship("PatientProgress", back_populates="prescriptions")
    prescribe = relationship("Prescribe", back_populates="prescriptions")