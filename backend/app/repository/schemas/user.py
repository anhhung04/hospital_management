from sqlalchemy import (
    String,
    Integer,
    Date,
    Enum as DBEnum
)
from sqlalchemy.orm import mapped_column
from repository.schemas import Base, ObjectID
from permissions.user import UserRole


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(String, primary_key=True, index=True)
    ssn = mapped_column(Integer, unique=True, index=True)
    username = mapped_column(String, unique=True, index=True)
    password = mapped_column(String)
    role = mapped_column(DBEnum(UserRole))    
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