import random
import string
import uuid
import json
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from repository.schemas import Base
from repository import get_db, get_redis
from app import app
from repository.schemas.user import User

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

def gen_id():
    return str(uuid.uuid4())

def gen_ssn():
    return str(random.randint(1000000000, 9999999999))

def gen_phone_number():
    return str(random.randint(1000000000, 9999999999))

def gen_name():
    user_data = random.choice(USER_DB)
    f = user_data['first_name']
    l = user_data['last_name']
    return f, l

def insert_user(db, username=None, password=None, user_type=None, gender=None):
    u = username or gen_username()
    p = password or gen_password()
    ut = user_type or random.choice(['EMPLOYEE', 'PATIENT'])
    id = gen_id()
    f, l = gen_name()
    user = User(
        id=id,
        ssn=gen_ssn(),
        username=u,
        password=p,
        phone_number=gen_phone_number(),
        user_type=user_type,
        gender=gender or 'male',
        last_name=l,
        first_name=f,
        nation='Vietnam',
        province=random.choice(['Hà Nội', 'TP. Hồ Chí Minh', 'Đà Nẵng', 'Hải Phòng', 'Huế', 'Cần Thơ', 'Quảng Ninh', 'Hải Dương', 'Hưng Yên', 'Nam Định', 'Ninh Bình', 'Thái Bình', 'Vĩnh Phúc', 'Bắc Ninh', 'Hà Nam', 'Hà Tây', 'Hòa Bình', 'Hà Giang', 'Lào Cai', 'Lai Châu', 'Sơn La', 'Yên Bái', 'Tuyên Quang', 'Thái Nguyên', 'Phú Thọ', 'Bắc Giang', 'Bắc Kạn', 'Cao Bằng', 'Điện Biên', 'Lạng Sơn', 'Bắc Ninh', 'Bắc Giang', 'Bắc Kạn', 'Cao Bằng', 'Điện Biên', 'Lạng Sơn', 'Lai Châu', 'Sơn La', 'Yên Bái', 'Tuyên Quang', 'Thái Nguyên', 'Phú Thọ', 'Vĩnh Phúc', 'Hà Giang', 'Quảng Ninh', 'Bắc Ninh', 'Hà Nam', 'Hà Tây', 'Hòa Bình', 'Hà Nội', 'Hải Dương', 'Hưng Yên', 'Nam Định', 'Ninh Bình', 'Thái Bình', 'Hà Nam', 'Hà Tây', 'Hòa Bình', 'Hà Giang', 'Lào Cai', 'Lai Châu', 'Sơn La', 'Yên Bái', 'Tuyên Quang', 'Thái Nguyên', 'Phú Thọ', 'Vĩnh Phúc', 'Bắc Giang', 'Bắc Kạn', 'Cao Bằng', 'Điện Biên', 'Lạng Sơn', 'Bắc Ninh', 'Bắc Giang', 'Bắc Kạn', 'Cao Bằng', 'Điện Biên', 'Lạng Sơn', 'Lai Châu',]),
        district=random.choice([
            'Quận 1', 'Quận 2', 'Quận 3', 'Quận 4', 'Quận 5', 'Quận 6', 'Quận 7', 'Quận 8', 'Quận 9', 'Quận 10', 'Quận 11', 'Quận 12', 'Quận Bình Tân', 'Quận Bình Thạnh', 'Quận Gò Vấp', 'Quận Phú Nhuận', 'Quận Tân Bình', 'Quận Tân Phú', 'Quận Thủ Đức', 'Huyện Bình Chánh', 'Huyện Cần Giờ', 'Huyện Củ Chi', 'Huyện Hóc Môn', 'Huyện Nhà Bè'
        ]),
        ward=random.choice([
            'Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5'
        ]),address = 'Số 268, Lý Thường Kiệt'
    )
    db.add(user)
    db.commit()
    return user


