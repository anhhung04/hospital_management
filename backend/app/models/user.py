from pydantic import BaseModel
from models.response import BaseResponseModel
from typing import Optional

class UserAuth(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: str


class ChangePasswordModel(BaseModel):
    old_password: str
    new_password: str
    

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
    phone_number: Optional[str]
    birth_date: Optional[str]
    gender: Optional[str]
    health_insurance: Optional[str]
    last_name: Optional[str]
    first_name: Optional[str]
    address: Optional[str]

class UserDetailResponse(BaseResponseModel):
    data: UserDetail


class PatchUserPrivateInfoModel(PatchUserDetailModel):
    password: Optional[str]
    username: Optional[str]

class QueryUserModel(BaseModel):
    username: Optional[str] = None
    id: Optional[str] = None
    ssn: Optional[str] = None
    email: Optional[str] = None
