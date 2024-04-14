from sqlalchemy import String, Date, ForeignKey, Integer, Time, Table, Column
from sqlalchemy import Enum as DBEnum
from sqlalchemy.orm import mapped_column, relationship, Mapped
from enum import Enum
from permissions.user import EmployeeType
from repository.schemas import Base, ObjectID
from repository.schemas.warehouse import employee_manage_container, Container
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

class Frequency(Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'

class ScheduleStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'
    SUSPENDED = 'suspended'
    INPROGRESS = 'in progress'

class FixedSchedule(Base):
    __tablename__ = 'fixed_schedules'
    
    id = mapped_column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    title = mapped_column(String)
    day = mapped_column(String)
    begin_time = mapped_column(Time)
    end_time = mapped_column(Time)
    begin_date = mapped_column(Date)
    end_date = mapped_column(Date)
    frequency = mapped_column(DBEnum(Frequency))

class OvertimeSchedule(Base):
    __tablename__ = 'overtime_schedules'

    id = mapped_column(Integer, primary_key=True,
                          index=True, autoincrement=True)
    title = mapped_column(String)
    date = mapped_column(Date)
    begin_time = mapped_column(Time)
    end_time = mapped_column(Time)
    
fixed_schedule_of_employee = Table(
    "employee_fixed_schedules", Base.metadata,
    Column("employee_id", ObjectID, ForeignKey("employees.user_id")),
    Column("schedule_id", Integer, ForeignKey("fixed_schedules.id")),
    Column("status", DBEnum(ScheduleStatus), default = ScheduleStatus.ACTIVE),
    extend_existing=True
)

overtime_schedule_of_employee = Table(
    "employee_overtime_schedules", Base.metadata,
    Column("employee_id", ObjectID, ForeignKey("employees.user_id")),
    Column("schedule_id", Integer, ForeignKey("overtime_schedules.id")),
    Column("status", DBEnum(ScheduleStatus), default = ScheduleStatus.ACTIVE),
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
    fixed_schedule: Mapped[List["FixedSchedule"]] = relationship(secondary=fixed_schedule_of_employee)
    overtime_schedule: Mapped[List["OvertimeSchedule"]] = relationship(secondary=overtime_schedule_of_employee)
    container_management: Mapped[List["Container"]] = relationship(secondary=employee_manage_container)

    __table_args__ = {"extend_existing": True}

