<<<<<<< Updated upstream
from sqlalchemy import Column, String
=======
from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
>>>>>>> Stashed changes
from repository.schemas import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
