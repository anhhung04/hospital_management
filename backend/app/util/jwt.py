from app import redis_client
from typing import Tuple
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.util.crypto import random_key

async def create_access_token(data: dict, userid: str, expire_minutes: int = 15) -> Tuple[str, Exception]:
    to_encode = data.copy()
    to_encode.update({"sub": userid})
    secret_key = random_key()
    try:
        redis_client.delete(userid)
        redis_client.set(userid, secret_key, ex=expire_minutes*60)
    except Exception as e:
        return None, e
    expire = datetime.now() + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm="HS256")
    return encoded_jwt, None

async def verify_token(token: str, userid: str) -> Tuple[str, Exception]:
    try:
        secret_key = redis_client.get(userid)
        if not secret_key:
            return None, Exception("Token expired")
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload, None
    except JWTError as e:
        return None, e
