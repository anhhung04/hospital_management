import redis
from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Request

engine = create_engine(config['POSTGRES_SQL_URL'])

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

REDIS_HOST = config["REDIS_HOST"]
REDIS_PORT = config["REDIS_PORT"]
MAX_CONNECTIONS_REDIS = config["MAX_CONNECTIONS_REDIS"]

redis_pool = redis.ConnectionPool(host=REDIS_HOST, port=int(REDIS_PORT), max_connections=MAX_CONNECTIONS_REDIS, db=0)

def get_db(request: Request):
    return request.state.db

def get_redis():
    r = redis.Redis(connection_pool=redis_pool)
    try:
        yield r
    finally:
        pass
