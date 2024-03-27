from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Medicine(Base):
    __tablename__ = 'medicines'

    medID = mapped_column(Integer, primary_key=True, index=True)
    containerID = mapped_column(Integer, ForeignKey('medical_warehouse_management.container_id'), index=True)
    medName = mapped_column(String)
    medType = mapped_column(String)
    medUnit = mapped_column(String)
    medPrice = mapped_column(Integer)
    medExpDate = mapped_column(Date)
    medQuantity = mapped_column(Integer)
    medical_warehouse_management = relationship("MedicalWarehouseManagement", back_populates="medicines")
    medicine_report = relationship("MedicineReport", back_populates="medicines")
