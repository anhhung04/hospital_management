import random
import string
from util.crypto import PasswordContext
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from repository.schemas import Base
from repository.schemas.user import User
from repository import Storage, RedisStorage
from permissions.user import UserRole
from uuid import uuid4
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

redis_cache = {}


class RedisLocal:
    def set(self, key, value, ex):
        print(key, value)
        redis_cache[key] = value

    def delete(self, key):
        if key in redis_cache:
            redis_cache.pop(key)
    def get(self, key):
        return redis_cache.get(key, None)


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


app.dependency_overrides[RedisStorage.get] = override_get_redis
app.dependency_overrides[Storage.get] = override_get_db

client = TestClient(app)


def gen_username():
    return ''.join(random.choices(string.ascii_lowercase, k=10))


def gen_password():
    return ''.join(random.choices(string.ascii_lowercase, k=10))


def create_user():
    username = gen_username()
    password = gen_password()
    return User(id=str(uuid4()), username=username, password=PasswordContext(password, username).hash(), role=UserRole.EMPLOYEE), password
