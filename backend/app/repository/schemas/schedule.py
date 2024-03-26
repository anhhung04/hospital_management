from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Schedule(Base):
    __tablename__ = 'schedules'

    employee_id = Column(Integer, ForeignKey('Employees.employee_id'), index=True)
    begin = Column(Date)
    end = Column(Date)
    status = Column(String)
    employee = relationship("Employee", back_populates="schedules", uselist=False)
    