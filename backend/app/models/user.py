from pydantic import BaseModel
from models.response import BaseResponse


class UserAuth(BaseModel):
    username: str
    password: str
    
class AccessResponse(BaseModel):
    access_token: str    
    
class UserAuthResponse(BaseResponse):
    data: AccessResponse