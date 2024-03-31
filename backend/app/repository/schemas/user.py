from sqlalchemy import (
    String,
    Enum as DBEnum
)
from sqlalchemy.orm import mapped_column
from repository.schemas import Base
from uuid import UUID
from permissions.user import UserRole


class ObjectID(String):
    def __instancecheck__(self, __instance: str) -> bool:
        try:
            UUID(__instance, version=4)
            return True
        except ValueError:
            return False

    def __repr__(self) -> str:
        return super().__repr__()


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(ObjectID, primary_key=True, index=True)
    username = mapped_column(String, unique=True, index=True)
    password = mapped_column(String)
    role = mapped_column(DBEnum(UserRole))
