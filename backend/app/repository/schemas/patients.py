from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Patient(Base):
    __tablename__ = 'patients'

    medID = mapped_column(Integer, primary_key=True, index=True, unique=True)
    user_id = mapped_column(String, ForeignKey('users.id'), index=True)
    medical_record_id = mapped_column(Integer, primary_key=True, index=True, unique=True)
    ssn = mapped_column(Integer, ForeignKey('users.ssn'), unique=True)
    weight = mapped_column(Integer)
    height = mapped_column(Integer)
    note = mapped_column(String)
    user = relationship("User", back_populates="patients", uselist=False)
    test_result = relationship("TestResult", back_populates="patients", uselist=False)
    patient_progress = relationship("PatientProgress", back_populates="patients", uselist=False)
    


