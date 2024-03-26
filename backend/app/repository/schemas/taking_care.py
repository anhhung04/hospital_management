from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class TakingCare(Base):
    __tablename__ = 'taking_care'

    nurse_id = Column(Integer, ForeignKey('nurse.nurse_id'), index=True)
    patient_id = Column(Integer, ForeignKey('patient.patient_id'), primary_key=True, index=True)
    employee = relationship("Employee", back_populates="taking_care")
