from pydantic import BaseModel
from models.response import BaseResponseModel


class UserAuth(BaseModel):
    username: str
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
    
class UserDetailResponse(BaseResponseModel):
    data: UserDetail
