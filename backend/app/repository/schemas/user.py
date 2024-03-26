from sqlalchemy import Table, Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    ssn = Column(Integer, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
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
    patient = relationship("Patient", back_populates="users", uselist=False)
    employee = relationship("Employee", back_populates="users", uselist=False)












    
