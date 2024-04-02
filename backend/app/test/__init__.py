import random
import string
import json
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from repository.schemas import Base
from repository.schemas.user import User
from repository.schemas.patient import Patient
from repository import Storage, RedisStorage
from uuid import uuid4
from app import app
from util.crypto import PasswordContext

USER_DB = json.loads(open('./test/data.json').read())

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
        nation='Vietnam',
        province=random.choice(['Hà Nội', 'TP. Hồ Chí Minh', 'Đà Nẵng', 'Hải Phòng', 'Huế', 'Cần Thơ', 'Quảng Ninh', 'Hải Dương', 'Hưng Yên', 'Nam Định', 'Ninh Bình', 'Thái Bình', 'Vĩnh Phúc', 'Bắc Ninh', 'Hà Nam', 'Hà Tây', 'Hòa Bình', 'Hà Giang', 'Lào Cai', 'Lai Châu', 'Sơn La', 'Yên Bái', 'Tuyên Quang', 'Thái Nguyên', 'Phú Thọ', 'Bắc Giang', 'Bắc Kạn', 'Cao Bằng', 'Điện Biên', 'Lạng Sơn', 'Bắc Ninh', 'Bắc Giang', 'Bắc Kạn', 'Cao Bằng', 'Điện Biên', 'Lạng Sơn', 'Lai Châu', 'Sơn La', 'Yên Bái', 'Tuyên Quang', 'Thái Nguyên', 'Phú Thọ', 'Vĩnh Phúc', 'Hà Giang', 'Quảng Ninh', 'Bắc Ninh', 'Hà Nam', 'Hà Tây', 'Hòa Bình', 'Hà Nội', 'Hải Dương', 'Hưng Yên', 'Nam Định', 'Ninh Bình', 'Thái Bình', 'Hà Nam', 'Hà Tây', 'Hòa Bình', 'Hà Giang', 'Lào Cai', 'Lai Châu', 'Sơn La', 'Yên Bái', 'Tuyên Quang', 'Thái Nguyên', 'Phú Thọ', 'Vĩnh Phúc', 'Bắc Giang', 'Bắc Kạn', 'Cao Bằng', 'Điện Biên', 'Lạng Sơn', 'Bắc Ninh', 'Bắc Giang', 'Bắc Kạn', 'Cao Bằng', 'Điện Biên', 'Lạng Sơn', 'Lai Châu',]),
        address='Số 268, Lý Thường Kiệt'
    )
    return user


def insert_user(db, username=None, password=None, user_type=None, gender=None):
    user = create_user(username, password, user_type, gender)
    db.add(user)
    db.commit()
    return user


def insert_patient(db, id=None, username=None, password=None):
    patient = Patient(user_id=id, weight=50, height=170, note='test')
    db.add(patient)
    db.commit()
    return patient
