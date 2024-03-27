from sqlalchemy import String
from sqlalchemy.orm import mapped_column
from repository.schemas import Base

class User(Base):
    __tablename__ = 'users'

    id = mapped_column(String, primary_key=True, index=True)
    username = mapped_column(String, unique=True, index=True)
    password = mapped_column(String)
