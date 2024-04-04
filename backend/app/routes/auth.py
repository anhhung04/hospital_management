from fastapi import APIRouter, status, HTTPException, Depends
from models.user import UserAuth, UserAuthResponse, VerifyTokenRequest, VerifyTokenReponse, LogoutResponseModel, UserDetailResponse, ChangePasswordResponse
from util.response import APIResponse
from services.auth import AuthService
from util.jwt import JWTHandler
from typing import Annotated
from pydantic import Field

router = APIRouter()


@router.post("/login", response_model=UserAuthResponse, tags=["auth"])
async def login(
    auth_req: UserAuth,
    service: AuthService = Depends(AuthService)
):
    try:
        token = await service.gen_token(auth_req)
    except HTTPException as e:
        return APIResponse.as_json(e.status_code, str(e.detail))
    return APIResponse.as_json(
        status.HTTP_200_OK, "login successful", {"access_token": token}
    )


@router.post("/verify", response_model=VerifyTokenReponse, tags=["auth"])
async def verify_user_token(
    verify_req: VerifyTokenRequest,
    jwt_handler: JWTHandler = Depends(JWTHandler)
):
    try:
        token_data = jwt_handler.verify(verify_req.access_token)
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
    old_password: Annotated[str, Field(description="old password", max_length=255)],
    new_password: Annotated[str, Field(
        description="new password", max_length=255)],
    service: AuthService = Depends(AuthService)
):
    try:
        await service.change_password(
            old_password,
            new_password
        )
    except HTTPException as e:
        return APIResponse.as_json(e.status_code, str(e.detail), {"success": False})
    return APIResponse.as_json(status.HTTP_200_OK, "change password successful", {"success": True})


@router.post('/logout', response_model=LogoutResponseModel, tags=["auth"])
async def log_out(
    service: AuthService = Depends(AuthService)
):
    try:
        await service.logout()
    except HTTPException as e:
        return APIResponse.as_json(e.status_code, str(e.detail), {"success": False})
    return APIResponse.as_json(status.HTTP_200_OK, "logout successful", {"success": True})


@router.get('/me', response_model=UserDetailResponse, tags=["auth"])
async def get_detail(
    service: AuthService = Depends(AuthService)
):
    try:
        user_detail = await service.get_user()
    except HTTPException as e:
        return APIResponse.as_json(e.status_code, str(e.detail))
    return APIResponse.as_json(
        status.HTTP_200_OK,
        "get user detail successful",
        user_detail.model_dump()
    )
