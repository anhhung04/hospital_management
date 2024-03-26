from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class Person(Base):
    __tablename__ = 'personal_infos'

    ssn = Column(Integer, primary_key=True, index=True)
    phone_number = Column(Integer)
    gender = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    birth_date = Column(Date)
    nation = Column(String)
    medID = Column(Integer)
    province = Column(String)
    district = Column(String)
    ward = Column(String)
    address = Column(String)
    patient = relationship("Patient", back_populates="person", uselist=False)
    employees = relationship("Employees", back_populates="person", uselist=False)