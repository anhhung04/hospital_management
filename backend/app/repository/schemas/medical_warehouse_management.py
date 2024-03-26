from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class MedicalWarehouseManagement(Base):
    __tablename__ = 'medical_warehouse_management'

    container_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    import_date = Column(Date)
    export_date = Column(Date)
    employees = relationship("Employees", back_populates="medical_warehouse_management")
    facility = relationship("Facility", back_populates="medical_warehouse_management")
    medicine = relationship("Medicine", back_populates="medical_warehouse_management")
    prescribe = relationship("Prescribe", back_populates="medical_warehouse_management") #cấn chỗ ni