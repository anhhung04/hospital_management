from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from repository.schemas import Base

class TakeCareOf(Base):
    __tablename__ = 'take_care_of'

    nurse_id = mapped_column(Integer, ForeignKey('employees.employee_id'), index=True)
    patient_id = mapped_column(Integer, ForeignKey('patients.medID'), primary_key=True, index=True)
    employee = relationship("Employee", back_populates="take_care_of")
    patient = relationship("Patient", back_populates="take_care_of")