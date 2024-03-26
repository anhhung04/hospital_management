from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base
#coi lại class ni
class Prescribe(Base): 
    __tablename__ = 'prescribe'

    number_of_drugs = Column(Integer)
    medicine_id = Column(Integer)
    prescription_id = Column(Integer, ForeignKey('prescription.prescription_id'), primary_key=True, index=True)
    num_of_drugs_per_time = Column(Integer)
    container_id = Column(Integer, ForeignKey('medical_warehouse_management.container_id'), index=True)
    prescription = relationship("Prescription", back_populates="prescribe")
    medical_warehouse_management = relationship("MedicalWarehouseManagement", back_populates="prescribe")