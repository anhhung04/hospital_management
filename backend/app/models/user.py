from pydantic import BaseModel, validator
from models.response import BaseResponseModel
from typing import Optional
from datetime import datetime

class UserAuth(BaseModel):
    email: Optional[str | None] = None
    username: Optional[str | None] = None
    password: str

class ChangePasswordStateModel(BaseModel):
    success: bool

class ChangePasswordResponse(BaseResponseModel):
    data: ChangePasswordStateModel

class VerifyTokenRequest(BaseModel):
    access_token: str


class AccessResponse(BaseModel):
    access_token: str


class UserAuthResponse(BaseResponseModel):
    data: AccessResponse


class VerifyUserReponseData(BaseModel):
    is_login: bool
    username: str
    user_id: str


class VerifyTokenReponse(BaseResponseModel):
    data: VerifyUserReponseData


class LogoutData(BaseModel):
    success: bool


class LogoutResponseModel(BaseResponseModel):
    data: LogoutData


class UserDetail(BaseModel):
    id: str
    ssn: str
    phone_number: str
    birth_date: str
    gender: str
    health_insurance: str
    last_name: str
    first_name: str
    address: str
    email: str
    username: str
    role: str

    @validator('birth_date', pre=True)
    def validate_birth_date(cls, v):
        if v and isinstance(v, datetime):
            return v.strftime("%d-%m-%Y")
        return str(v)


class AddUserDetailModel(UserDetail):
    password: str

class AddUserModel(BaseModel):
    first_name: str
    last_name: str
    birth_date: str
    gender: str
    ssn: str
    phone_number: str
    address: str
    email: str
    health_insurance: str


class PatchUserDetailModel(BaseModel):
    phone_number: Optional[str | None] = None
    birth_date: Optional[str | None] = None
    gender: Optional[str | None] = None
    health_insurance: Optional[str | None] = None
    last_name: Optional[str | None] = None
    first_name: Optional[str | None] = None
    address: Optional[str | None] = None

class UserDetailResponse(BaseResponseModel):
    data: UserDetail


class PatchUserPrivateInfoModel(PatchUserDetailModel):
    password: Optional[str | None] = None
    username: Optional[str | None] = None

class QueryUserModel(BaseModel):
    username: Optional[str | None] = None
    id: Optional[str | None] = None
    ssn: Optional[str | None] = None
    email: Optional[str | None] = None
