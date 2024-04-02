from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String
from uuid import UUID

Base = declarative_base()

class ObjectID(String):
    def __instancecheck__(self, __instance: str) -> bool:
        try:
            UUID(__instance, version=4)
            return True
        except ValueError:
            return False

    def __repr__(self) -> str:
        return super().__repr__()