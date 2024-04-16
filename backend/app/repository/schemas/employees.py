from sqlalchemy import String, Date, ForeignKey, Time, Integer, Boolean, Table, Column
from sqlalchemy import Enum as DBEnum
from sqlalchemy.orm import mapped_column, relationship, Mapped
from enum import Enum
from permissions.user import EmployeeType
from repository.schemas import Base, ObjectID
from typing import List

class EducateLevel(Enum):
    BACHELOR = 'BACHELOR'
    MASTER = 'MASTER'
    DOCTOR = 'DOCTOR'
    UNDERGRADUATE = 'UNDERGRADUATE'
    UNKNOWN = 'UNKNOWN'


class EmployeeStatus(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    PENDING = 'PENDING'
    SUSPENDED = 'SUSPENDED'
    WIP = 'WIP'

class DayOfWeek(Enum):
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'

class Frequency(Enum):
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    YEARLY = 'YEARLY'

class ScheduleStatus(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    PENDING = 'PENDING'
    SUSPENDED = 'SUSPENDED'
    INPROGRESS = 'INPROGRESS'

class Event(Base):
    __tablename__ = 'events'
    id = mapped_column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    title = mapped_column(String)
    day_of_week = mapped_column(DBEnum(DayOfWeek))
    begin_time = mapped_column(Time)
    end_time = mapped_column(Time)
    begin_date = mapped_column(Date)
    end_date = mapped_column(Date)
    is_recurring = mapped_column(Boolean)
    frequency = mapped_column(DBEnum(Frequency))
    employee: Mapped["Employee"] = relationship("Employee", secondary="schedules", back_populates="event", lazy="select")

schedule = Table(
    "schedules", Base.metadata,
    Column("employee_id", ObjectID, ForeignKey("employees.user_id")),
    Column("event_id", Integer, ForeignKey("events.id")),
    extend_existing=True
)
    

class Employee(Base):
    __tablename__ = 'employees'

    user_id = mapped_column(ObjectID, ForeignKey('users.id'), primary_key=True)
    employee_type = mapped_column(DBEnum(EmployeeType))
    education_level = mapped_column(DBEnum(EducateLevel))
    begin_date = mapped_column(Date)
    end_date = mapped_column(Date)
    faculty = mapped_column(String)
    status = mapped_column(DBEnum(EmployeeStatus))
    personal_info = relationship("User", primaryjoin="Employee.user_id == User.id", uselist=False)
    event: Mapped[List["Event"]] = relationship("Event", secondary="schedules", back_populates="employee", lazy="select")
    __table_args__ = {"extend_existing": True}