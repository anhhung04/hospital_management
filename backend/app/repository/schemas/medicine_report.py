from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class MedicineReport(Base):
    __tablename__ = 'medicine_report'

    medID = Column(Integer, ForeignKey('medicine.medID'), primary_key=True, index=True)
    medName = Column(String)
    medType = Column(String)
    medPrice = Column(Integer)
    medExpDate = Column(Date)
    medQuantity = Column(Integer)
    import_date = Column(Date)
    export_date = Column(Date)
    quantity_added = Column(Integer)
    medicine = relationship("Medicine", back_populates="medicine_report")