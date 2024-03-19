from sqlalchemy import Column, Integer, String, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

__all__ = ["User"]