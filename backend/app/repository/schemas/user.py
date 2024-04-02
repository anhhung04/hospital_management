from sqlalchemy import (
    String,
    Integer,
    Date,
    Enum as DBEnum
)
from sqlalchemy.orm import mapped_column
from repository.schemas import Base, ObjectID
from permissions.user import UserRole
import re

class Email(String):
    def __instancecheck__(self, __instance: str) -> bool:
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(email_regex, __instance) is not None

    def __repr__(self) -> str:
        return super().__repr__()

class SSN(String):
    def __instancecheck__(self, __instance: str) -> bool:
        ssn_regex = r'^\d{12}$'
        return re.fullmatch(ssn_regex, __instance) is not None

    def __repr__(self) -> str:
        return super().__repr__()


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(ObjectID, primary_key=True, index=True)
    ssn = mapped_column(SSN, unique=True, index=True)
    phone_number = mapped_column(String)
    birth_date = mapped_column(Date)
    gender = mapped_column(String)
    health_insurance = mapped_column(String)
    last_name = mapped_column(String)
    first_name = mapped_column(String)
    nation = mapped_column(String)
    province = mapped_column(String)
    city = mapped_column(String)
    address = mapped_column(String)
    email = mapped_column(Email, unique=True)
    username = mapped_column(String, unique=True, index=True)
    password = mapped_column(String)
    role = mapped_column(DBEnum(UserRole))   
    
    
    