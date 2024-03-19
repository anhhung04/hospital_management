import random
import string
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from repository.schemas import Base
from repository import get_db, get_redis
from app import app


SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


class RedisLocal:
    cache: dict

    def __init__(self):
        self.cache = {}

    def set(self, key, value, ex):
        self.cache[key] = value

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def get(self, key):
        return self.cache.get(key)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def override_get_redis():
    try:
        yield RedisLocal()
    finally:
        pass


app.dependency_overrides[get_redis] = override_get_redis
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def gen_username():
    return ''.join(random.choices(string.ascii_lowercase, k=10))


def gen_password():
    return ''.join(random.choices(string.ascii_lowercase, k=10))

