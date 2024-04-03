from sqlalchemy.orm import Session
from redis import Redis
from models.user import UserAuth
from typing import Tuple
from util.jwt import JWTHandler, JWTPayload
from util.crypto import PasswordContext
from repository.user import UserRepo, GetUserQuery
from repository.schemas.user import User
from models.user import UserDetail
from services import IService
from permissions.user import UserRole
from permissions import Permission


class AuthService(IService):
    def __init__(self, session: Session, user: dict, redis_client: Redis):
        super().__init__(session, user, redis_client)
        self._user_repo = UserRepo(session)

    async def gen_token(self, auth_request: UserAuth) -> Tuple[str, str]:
        user: User = await self._user_repo.get(
            query=GetUserQuery(None, auth_request.username)
        )
        if not user:
            return None, "Nonexistent user"
        if not PasswordContext(auth_request.password, auth_request.username).verify(user.password):
            return None, "Invalid username or password"
        token, err = JWTHandler(redis_client=self._rc).create(
            payload=JWTPayload(user.username, user.id, user.role)
        )
        if err:
            return None, err
        return token, None

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE, UserRole.PATIENT])
    async def get_user(self) -> User:
        if not self._current_user:
            return None, "User is not logged in"
        user = await self._user_repo.get(query=GetUserQuery(
            self._current_user.get('sub'), None))
        if not user:
            return None, "Nonexistent user"
        user = UserDetail.model_validate(
            {c.name: str(getattr(user, c.name)) for c in user.__table__.columns})
        return user, None

    async def logout(self) -> str:
        try:
            if self._current_user:
                await self._rc.delete(self._current_user.get('sub'))
                return None
            return "User is not logged in"
        except Exception as e:
            return e

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE, UserRole.PATIENT])
    async def change_password(self, old_password: str, new_password: str) -> str:
        user = await self._user_repo.get(query=GetUserQuery(
            self._current_user.get('sub'), None))
        if not user:
            return "Nonexistent user"
        if not PasswordContext(old_password, user.username).verify(user.password):
            return "Invalid password"
        user_update = await self._user_repo.update(query=GetUserQuery(
            self._current_user.get('sub'), None), update_item={
            "password": PasswordContext(new_password, user.username).hash()
        })
        if not user_update:
            return "Failed to update password"
        return None
