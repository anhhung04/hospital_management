from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Facility(Base):
    __tablename__ = 'facilities'

    facility_id = mapped_column(Integer, primary_key=True, index=True)
    container_id = mapped_column(Integer, ForeignKey('medical_warehouse_management.container_id'), index=True)
    facility_name = mapped_column(String)
    availability = mapped_column(String)
    maintanance_date = mapped_column(Date)
    medical_warehouse_management = relationship("MedicalWarehouseManagement", back_populates="facilities")