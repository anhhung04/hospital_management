from sqlalchemy import Table, String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class TakingCare(Base):
    __tablename__ = 'taking_care'

    nurse_id = mapped_column(Integer, ForeignKey('employees.employee_id'), index=True)
    patient_id = mapped_column(Integer, ForeignKey('patients.medID'), primary_key=True, index=True)
    employee = relationship("Employee", back_populates="taking_care")
