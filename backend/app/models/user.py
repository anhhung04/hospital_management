from pydantic import BaseModel
from models.response import BaseResponse


class UserAuth(BaseModel):
    username: str
    password: str
    

class VerifyTokenRequest(BaseModel):
    access_token: str
    
class AccessResponse(BaseModel):
    access_token: str    
    
class UserAuthResponse(BaseResponse):
    data: AccessResponse
    
class VerifyUserReponseData(BaseModel):
    is_login: bool
    username: str
    user_id: str


class VerifyTokenReponse(BaseResponse):
    data: VerifyUserReponseData