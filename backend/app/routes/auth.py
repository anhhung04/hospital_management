from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from models.user import UserAuth, UserAuthResponse, VerifyTokenRequest, VerifyTokenReponse, LogoutResponseModel
from models.request import TokenHeader
from util.response import APIResponse
from repository import Storage, RedisStorage
from services.auth import AuthService
from util.jwt import JWTHandler

router = APIRouter()

@router.post("/login", response_model=UserAuthResponse)
async def login(auth_req: UserAuth, db_sess: Session = Depends(Storage.get), redis_client=Depends(RedisStorage.get)):
    token, err = await AuthService(db_sess, redis_client).gen_token(auth_req)
    if err:
        return APIResponse.as_json(status.HTTP_401_UNAUTHORIZED, str(err), {})
    return APIResponse.as_json(
        status.HTTP_200_OK, "login successful", {"access_token": token}
    )


@router.post("/verify", response_model=VerifyTokenReponse)
async def verify_user_token(verify_req: VerifyTokenRequest, redis_client=Depends(RedisStorage.get)):
    token_data, err = JWTHandler(redis_client).verify(verify_req.access_token)
    if err:
        return APIResponse.as_json(
            status.HTTP_401_UNAUTHORIZED,
            str(err),
            {
                "is_login": False,
                "username": "",
                "user_id": "",
            },
        )
    return APIResponse.as_json(
        status.HTTP_200_OK,
        "verify successful",
        {
            "is_login": True,
            "username": token_data["info"]["username"],
            "user_id": token_data["sub"],
        },
    )


@router.post('/logout', response_model=LogoutResponseModel)
async def log_out(
    token: TokenHeader,
    db_sess: Session = Depends(Storage.get),
    redis_client=Depends(RedisStorage.get)
):
    err = await AuthService(db_sess, redis_client).logout(token)
    if err:
        return APIResponse.as_json(status.HTTP_401_UNAUTHORIZED, str(err), {"success": False})
    return APIResponse.as_json(status.HTTP_200_OK, "logout successful", {"success": True})
