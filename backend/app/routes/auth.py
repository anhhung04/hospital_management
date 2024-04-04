from fastapi import APIRouter, Depends, status, Request, HTTPException
from sqlalchemy.orm import Session
from models.user import UserAuth, UserAuthResponse, VerifyTokenRequest, VerifyTokenReponse, LogoutResponseModel, UserDetailResponse, ChangePasswordModel, ChangePasswordResponse
from util.response import APIResponse
from repository import Storage, RedisStorage
from services.auth import AuthService
from util.jwt import JWTHandler

router = APIRouter()


@router.post("/login", response_model=UserAuthResponse, tags=["auth"])
async def login(
    auth_req: UserAuth,
    db_sess: Session = Depends(Storage.get),
    redis_client=Depends(RedisStorage.get)
):
    try:
        token = await AuthService(db_sess, None, redis_client).gen_token(auth_req)
    except HTTPException as e:
        return APIResponse.as_json(e.status_code, str(e.detail))
    return APIResponse.as_json(
        status.HTTP_200_OK, "login successful", {"access_token": token}
    )


@router.post("/verify", response_model=VerifyTokenReponse, tags=["auth"])
async def verify_user_token(verify_req: VerifyTokenRequest, redis_client=Depends(RedisStorage.get)):
    try:
        token_data = JWTHandler(redis_client).verify(verify_req.access_token)
    except HTTPException as e:
        return APIResponse.as_json(e.status_code, str(e.detail), {"is_login": False})
    return APIResponse.as_json(
        status.HTTP_200_OK,
        "verify successful",
        {
            "is_login": True,
            "username": token_data["info"]["username"],
            "user_id": token_data["sub"],
        },
    )


@router.post("/password/change", response_model=ChangePasswordResponse, tags=["auth"])
async def changge_password(
    change_pass_request: ChangePasswordModel,
    request: Request,
    db_sess: Session = Depends(Storage.get),
    redis_client=Depends(RedisStorage.get)
):
    try:
        await AuthService(db_sess, request.state.user, redis_client).change_password(
            change_pass_request.old_password,
            change_pass_request.new_password
        )
    except HTTPException as e:
        return APIResponse.as_json(e.status_code, str(e.detail), {"success": False})
    return APIResponse.as_json(status.HTTP_200_OK, "change password successful", {"success": True})


@router.post('/logout', response_model=LogoutResponseModel, tags=["auth"])
async def log_out(request: Request, redis_client=Depends(RedisStorage.get)):
    try:
        await AuthService(None, request.state.user, redis_client).logout()
    except HTTPException as e:
        return APIResponse.as_json(e.status_code, str(e.detail), {"success": False})
    return APIResponse.as_json(status.HTTP_200_OK, "logout successful", {"success": True})


@router.get('/me', response_model=UserDetailResponse, tags=["auth"])
async def get_detail(
    request: Request,
    db_sess: Session = Depends(Storage.get),
    redis_client=Depends(RedisStorage.get)
):
    try:
        user_detail = await AuthService(db_sess, request.state.user, redis_client).get_user()
    except HTTPException as e:
        return APIResponse.as_json(e.status_code, str(e.detail))
    return APIResponse.as_json(
        status.HTTP_200_OK,
        "get user detail successful",
        user_detail.model_dump()
    )
