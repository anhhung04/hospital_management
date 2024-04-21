from typing import Tuple
from jose import jwt, JWTError
from datetime import datetime, timedelta
from util.crypto import PasswordContext
from util.log import logger
from redis import Redis
from repository import RedisStorage
from collections import namedtuple
from repository.schemas.user import ObjectID
from fastapi import HTTPException, status, Depends

JWTPayload = namedtuple("JWTPayload", ["username", "id", "role"])


class JWTHandler:
    def __init__(
        self,
        redis_client: Redis = Depends(RedisStorage.get)
    ):
        self._rc = redis_client
        self._expire_minutes = 1440

    def create(self, payload: JWTPayload) -> Tuple[str, Exception]:
        secret_key: str = PasswordContext.rand_key()
        try:
            self._rc.delete(str(payload.id))
            self._rc.set(str(payload.id),
                         str(secret_key),
                         ex=self._expire_minutes*60)
        except Exception as e:
            logger.error("create_access_token error", reason=str(e))
            return str(None), e
        expire = datetime.now().__add__(timedelta(minutes=self._expire_minutes))
        jwt_payload = {
            "sub": str(payload.id),
            "exp": expire.timestamp(),
            "info": {
                "username": payload.username,
                "role": str(payload.role),
            },
        }
        token: str = jwt.encode(jwt_payload, secret_key, algorithm="HS256")
        return token, None

    def verify(self, token: str) -> dict:
        try:
            jwt_payload: dict = jwt.get_unverified_claims(token)
            user_id: ObjectID = jwt_payload.get('sub', None)
            exp_time: datetime = datetime.fromtimestamp(
                float(jwt_payload.get('exp', 0))
            )
            if exp_time.__le__(datetime.now()):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired!"
                )
            secret_key = self._rc.get(user_id)
            if not secret_key:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token invalid!"
                )
            payload: dict = jwt.decode(token, secret_key, algorithms=["HS256"])
            return payload
        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=e
            )

    @staticmethod
    def unverify_decode(token: str) -> dict:
        try:
            return jwt.get_unverified_claims(token)
        except JWTError:
            return {}
