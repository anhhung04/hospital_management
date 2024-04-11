from redis import Redis
from models.user import UserAuth
from util.jwt import JWTHandler, JWTPayload
from util.crypto import PasswordContext
from repository.user import UserRepo
from models.user import UserDetail, QueryUserModel, PatchUserPrivateInfoModel
from permissions.user import UserRole
from permissions import Permission
from fastapi import HTTPException, status, Depends
from repository import RedisStorage
from middleware.user_ctx import UserContext


class AuthService:
    def __init__(
        self,
        user: UserContext = Depends(UserContext),
        redis_client: Redis = Depends(RedisStorage.get),
        user_repo: UserRepo = Depends(UserRepo)
    ):
        self._user_repo = user_repo
        self._current_user = user
        self._rc = redis_client

    async def gen_token(self, auth_request: UserAuth) -> str:
        user, err = await self._user_repo.get(
            QueryUserModel(
                username=auth_request.username,
                email=auth_request.email
            )
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Nonexistent user"
            )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        if not PasswordContext(auth_request.password, auth_request.username).verify(user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid password"
            )
        token, err = JWTHandler(redis_client=self._rc).create(
            payload=JWTPayload(user.username, user.id, user.role)
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to generate token"
            )
        return token

    @Permission.permit([UserRole.EMPLOYEE, UserRole.PATIENT])
    async def get_user(self) -> dict:
        if not self._current_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User is not logged in"
            )
        user, err = await self._user_repo.get(
            QueryUserModel(id=self._current_user.id())
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(err)
            )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return UserDetail.model_validate({
            c.name: str(getattr(user, c.name)) for c in user.__table__.columns
        })

    async def logout(self) -> str:
        try:
            user_id = self._current_user.id()
            if not user_id:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User is not logged in"
                )
            self._rc.delete(user_id)
            return None
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to logout user"
            )

    @Permission.permit([UserRole.EMPLOYEE, UserRole.PATIENT])
    async def change_password(
        self,
        old_password: str,
        new_password: str
    ) -> dict:
        user, err = await self._user_repo.get(
            QueryUserModel(id=self._current_user.id())
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        if not PasswordContext(old_password, user.username).verify(user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid password"
            )
        user_update, err = await self._user_repo.update(
            QueryUserModel(id=self._current_user.id()),
            PatchUserPrivateInfoModel(password=new_password)
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update password"
            )
        return UserDetail.model_validate({
            c.name: str(getattr(user_update, c.name)) for c in user_update.__table__.columns
        }).model_dump()
