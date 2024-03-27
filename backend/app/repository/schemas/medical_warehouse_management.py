from sqlalchemy import Integer, Date, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from repository.schemas import Base

class MedicalWarehouseManagement(Base):
    __tablename__ = 'medical_warehouse_management'

    container_id = mapped_column(Integer, primary_key=True, index=True)
    employee_id = mapped_column(Integer, ForeignKey('employees.employee_id'))
    import_date = mapped_column(Date)
    export_date = mapped_column(Date)
    employee = relationship("Employee", back_populates="medical_warehouse_management")
    facility = relationship("Facility", back_populates="medical_warehouse_management")
    medicine = relationship("Medicine", back_populates="medical_warehouse_management")
    prescribe = relationship("Prescribe", back_populates="medical_warehouse_management")