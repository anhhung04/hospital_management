from sqlalchemy import Table, String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from repository.schemas import Base

class User(Base):
    __tablename__ = 'users'

    id = mapped_column(String, primary_key=True, index=True)
    ssn = mapped_column(Integer, unique=True, index=True)
    username = mapped_column(String, unique=True, index=True)
    password = mapped_column(String)
    phone_number = mapped_column(Integer)
    gender = mapped_column(String)
    last_name = mapped_column(String)
    first_name = mapped_column(String)
    birth_date = mapped_column(Date)
    nation = mapped_column(String)
    province = mapped_column(String)
    district = mapped_column(String)
    ward = mapped_column(String)
    address = mapped_column(String)
    patient = relationship("Patient", back_populates="users", uselist=False)
    employee = relationship("Employee", back_populates="users", uselist=False)












    
