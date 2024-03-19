from sqlalchemy import Column, String
from repository.schemas import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
