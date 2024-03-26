from repository import get_redis
from typing import Tuple
from jose import JWTError, jwt
from datetime import datetime, timedelta
from util.crypto import random_key
from util.log import logger
from redis import Redis


def create_access_token(redis_client: Redis, data: dict, userid: str, expire_minutes: int = 15, ) -> Tuple[str, Exception]:
    data.update({"sub": userid})
    secret_key = random_key()
    try:
        redis_client.delete(userid)
        redis_client.set(userid, secret_key, ex=expire_minutes*60)
    except Exception as e:
        logger.error(f"create_access_token error")
        return None, e
    expire = datetime.now() + timedelta(minutes=expire_minutes)
    data.update({"exp": expire.timestamp()})
    encoded_jwt = jwt.encode(data, secret_key, algorithm="HS256")
    return encoded_jwt, None


def verify_token(token: str, userid: str) -> Tuple[str, Exception]:
    try:
        secret_key = redis_client.get(userid)
        if not secret_key:
            return None, Exception("Token expired")
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload, None
    except JWTError as e:
        logger.error(f"verify_token error: %s")
        return None, e
