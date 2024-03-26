from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class TestResult(Base):
    __tablename__ = 'test_results'

    test_id = Column(Integer, primary_key=True, index=True)
    medical_record_id = Column(Integer, ForeignKey('patient.medical_record_id'))
    test_date = Column(Date)
    test_result = Column(String)
    test_type = Column(String)
    patient = relationship("Patient", back_populates="test_results", uselist=False)