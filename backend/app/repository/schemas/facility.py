from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Facility(Base):
    __tablename__ = 'facility'

    facility_id = Column(Integer, ForeignKey('medical_warehouse_management.container_id'), primary_key=True, index=True)
    facility_name = Column(String)
    availability = Column(String)
    maintanance_date = Column(Date)
    medical_warehouse_management = relationship("MedicalWarehouseManagement", back_populates="facility")