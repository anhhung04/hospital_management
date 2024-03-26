from sqlalchemy import Table, String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class TestResult(Base):
    __tablename__ = 'test_results'

    test_id = mapped_column(Integer, primary_key=True, index=True)
    medical_record_id = mapped_column(Integer, ForeignKey('patients.medical_record_id'))
    test_date = mapped_column(Date)
    test_result = mapped_column(String)
    test_type = mapped_column(String)
    patient = relationship("Patient", back_populates="test_results", uselist=False)