from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from models.user import UserAuth, UserAuthResponse, UserToken, VerifyUserReponse
from util.response import wrap_response
from repository import get_db, get_redis
from services.auth import get_access_token
from util.jwt import verify_token

router = APIRouter()

@router.post("/login", response_model=UserAuthResponse)
async def login(user_auth: UserAuth, db: Session = Depends(get_db), redis_client=Depends(get_redis)):
    access_token, err = await get_access_token(db, redis_client, user_auth)
    if err:
        return wrap_response(status.HTTP_401_UNAUTHORIZED, str(err), {})
    return wrap_response(
        status.HTTP_200_OK, "login successful", {"access_token": access_token}
    )


@router.post("/verify", response_model=VerifyUserReponse)
async def verify_user_token(token: UserToken, redis_client=Depends(get_redis)):
    token_data, err = verify_token(redis_client, token.access_token)
    if err:
        return wrap_response(
            status.HTTP_401_UNAUTHORIZED,
            str(err),
            {
                "is_login": False,
                "username": "",
                "user_id": "",
            },
        )
    return wrap_response(
        status.HTTP_200_OK,
        "verify successful",
        {
            "is_login": True,
            "username": token_data["info"]["username"],
            "user_id": token_data["sub"],
        },
    )
