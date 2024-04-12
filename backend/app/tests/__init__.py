import random
import string
import json
from fastapi.testclient import TestClient
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from repository.schemas import Base
from repository.schemas.user import User
from repository.schemas.patient import Patient
from repository.schemas.employees import Employee
from repository import Storage, RedisStorage
from uuid import uuid4
from app import app
from util.crypto import PasswordContext
import requests

USER_DB = json.loads(open('./tests/data.json', errors="replace").read())

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


class TestIntegration(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._s = requests.session()
        self._base = "http://localhost:8000/api"
        self._route = None
        self._access_token = self._s.post(self._base + "/auth/login", json={
            "username": "employee1",
            "password": "demo"
        }).json()["data"]["access_token"]
        self._s.headers = {
            "Authorization": f"Bearer {self._access_token}"
        }

    def path(self, path):
        return self._base + self._route + path


def gen_username():
    return ''.join(random.choices(string.ascii_lowercase, k=10))


def gen_password():
    return ''.join(random.choices(string.ascii_lowercase, k=10))


def gen_id():
    return str(uuid4())


def gen_ssn():
    return str(random.randint(1000000000, 9999999999))


def gen_phone_number():
    return str(random.randint(1000000000, 9999999999))


def gen_name():
    user_data = random.choice(USER_DB)
    firstname = user_data['first_name']
    lastname = user_data['last_name']
    return firstname, lastname


def create_user(username=None, password=None, user_type=None, gender=None):
    u = username or gen_username()
    p = password or gen_password()
    ut = user_type or random.choice(['EMPLOYEE', 'PATIENT'])
    id = gen_id()
    first_name, last_name = gen_name()
    user = User(
        id=id,
        ssn=gen_ssn(),
        username=u,
        password=PasswordContext(p, u).hash(),
        phone_number=gen_phone_number(),
        role=ut,
        gender=gender or 'male',
        last_name=last_name,
        first_name=first_name,
        address='Số 268, Lý Thường Kiệt'
    )
    return user


def insert_user(db, username=None, password=None, user_type=None, gender=None):
    user = create_user(username, password, user_type, gender)
    db.add(user)
    db.commit()
    return user


def insert_patient(db, id=None, username=None, password=None):
    patient = Patient(user_id=id)
    db.add(patient)
    db.commit()
    return patient


def insert_employee(db, id=None, username=None, password=None):
    employee = Employee(user_id=id)
    db.add(employee)
    db.commit()
    return employee

def insert_employee_full(db, user_id, employee_type, education_level, begin_date, end_date, faculty, status):
    employee = Employee(
        user_id=user_id,
        employee_type=employee_type,
        education_level=education_level,
        begin_date=begin_date,
        end_date=end_date,
        faculty=faculty,
        status=status
    )
    db.add(employee)
    db.commit()
    return employee