from sqlalchemy import Table, String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Schedule(Base):
    __tablename__ = 'schedules'

    schedule_id = mapped_column(Integer, primary_key=True, index=True)
    employee_id = mapped_column(Integer, ForeignKey('employees.employee_id'), index=True)
    begin = mapped_column(Date)
    end = mapped_column(Date)
    status = mapped_column(String)
    employee = relationship("Employee", back_populates="schedules", uselist=False)
