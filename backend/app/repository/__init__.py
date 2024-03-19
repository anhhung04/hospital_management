import redis
from fastapi_sqlalchemy import db
from config import config

def get_db():
    _db = db.session
    try:
        yield _db
    finally:
        _db.close()

redis_client = redis.Redis(host=config['REDIS_HOST'], port=config['REDIS_PORT'], db=0)