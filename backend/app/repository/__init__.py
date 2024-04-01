import redis
from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException, Request


class IRepo:
    def create(self, item: object) -> object:
        pass

    def get(self, query: dict) -> object:
        pass

    def update(self, query: dict, update_item: object) -> object:
        pass

    def delete(self, query: dict) -> object:
        pass


engine = create_engine(config['POSTGRES_SQL_URL'])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

redis_pool: redis.ConnectionPool = redis.ConnectionPool(host=config["REDIS_HOST"], port=int(
    config["REDIS_PORT"]), max_connections=config["MAX_CONNECTIONS_REDIS"], db=0)


class Storage:
    @staticmethod
    def get():
        db = SessionLocal()
        try:
            yield db
        except Exception:
            raise HTTPException(
                status_code=500, detail=str("Database had error"))
        finally:
            db.close()


class RedisStorage:
    @staticmethod
    def get():
        r = redis.Redis(connection_pool=redis_pool)
        try:
            yield r
        except Exception:
            raise HTTPException(
                status_code=500, detail=str("Redis had error"))
        finally:
            pass
