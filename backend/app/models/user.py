from pydantic import BaseModel
from models.response import BaseResponseModel


class UserAuth(BaseModel):
    username: str
    password: str

class VerifyTokenRequest(BaseModel):
    access_token: str
    

class AccessResponse(BaseResponseModel):
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
