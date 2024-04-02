from sqlalchemy.orm import Session
from redis import Redis
from models.user import UserAuth
from typing import Tuple
from util.jwt import JWTHandler, JWTPayload
from util.crypto import PasswordContext
from repository.user import UserRepo, GetUserQuery
from repository.schemas.user import User


class AuthService:
    def __init__(self, session: Session, redis_client: Redis):
        self._sess = session
        self._rc = redis_client

    async def gen_token(self, auth_request: UserAuth) -> Tuple[str, str]:
        user: User = UserRepo(self._sess).get(
            query=GetUserQuery(None, auth_request.username)
        )
        if not user:
            return None, "Nonexistent user"
        if self._rc.get(str(user.id)):
            return None, "User already logged in"
        if not PasswordContext(auth_request.password, auth_request.username).verify(user.password):
            return None, "Invalid username or password"
        token, err = JWTHandler(redis_client=self._rc).create(
            payload=JWTPayload(user.username, user.id, user.role)
        )
        if err:
            return None, err
        return token, None

    async def logout(self, user_id: str) -> str:
        self._rc.delete(user_id)
        return None
