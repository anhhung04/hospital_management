from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Prescription(Base):
    __tablename__ = 'prescriptions'

    prescription_id = mapped_column(Integer, primary_key=True, index=True, unique=True)
    medical_record_id = mapped_column(Integer, primary_key=True, index=True)
    prescription_date = mapped_column(Date)
    quantity = mapped_column(Integer)
    dosage = mapped_column(String)
    usage = mapped_column(String)
    note = mapped_column(String)
    patient_progress = relationship("PatientProgress", back_populates="prescriptions")
    prescribe = relationship("Prescribe", back_populates="prescriptions")