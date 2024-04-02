from sqlalchemy import (
    String,
    Enum as DBEnum
)
from sqlalchemy.orm import mapped_column
from repository.schemas import Base, ObjectID
from permissions.user import UserRole


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(ObjectID, primary_key=True, index=True)
    username = mapped_column(String, unique=True, index=True)
    password = mapped_column(String)
    role = mapped_column(DBEnum(UserRole))
