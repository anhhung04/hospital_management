from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Patient(Base):
    __tablename__ = 'patients'

    medical_record_id = Column(Integer, primary_key=True, index=True)
    ssn = Column(Integer, ForeignKey('personal_infos.ssn'), unique=True)
    weight = Column(Integer)
    height = Column(Integer)
    note = Column(String)
    user = relationship("User", back_populates="patients", uselist=False)
    test_result = relationship("TestResult", back_populates="patients", uselist=False)
    patient_progress = relationship("PatientProgress", back_populates="patients", uselist=False)
    


