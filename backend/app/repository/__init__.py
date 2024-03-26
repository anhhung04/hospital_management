import redis
from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Request

engine = create_engine(config['POSTGRES_SQL_URL'])


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

redis_client = redis.Redis(
    host=config['REDIS_HOST'], port=config['REDIS_PORT'], db=0)


def get_db(request: Request):
    return request.state.db


def get_redis():
    r = redis_client
    try:
        yield r
    finally:
        pass
