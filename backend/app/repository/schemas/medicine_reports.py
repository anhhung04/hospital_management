from sqlalchemy import Table, String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class MedicineReport(Base):
    __tablename__ = 'medicine_reports'

    reportID = mapped_column(Integer, primary_key=True, index=True)
    medID = mapped_column(Integer, ForeignKey('medicines.medID'), index=True)
    medName = mapped_column(String)
    medType = mapped_column(String)
    medPrice = mapped_column(Integer)
    medExpDate = mapped_column(Date)
    medQuantity = mapped_column(Integer)
    import_date = mapped_column(Date)
    export_date = mapped_column(Date)
    quantity_added = mapped_column(Integer)
    medicine = relationship("Medicine", back_populates="medicine_reports")