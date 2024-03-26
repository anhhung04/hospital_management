from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Medicine(Base):
    __tablename__ = 'medicines'

    medID = Column(Integer, ForeignKey('medical_warehouse_management.container_id'), primary_key=True, index=True)
    medName = Column(String)
    medType = Column(String)
    medUnit = Column(String)
    medPrice = Column(Integer)
    medExpDate = Column(Date)
    medQuantity = Column(Integer)
    medical_warehouse_management = relationship("MedicalWarehouseManagement", back_populates="medicines")
    medicine_report = relationship("MedicineReport", back_populates="medicines")
