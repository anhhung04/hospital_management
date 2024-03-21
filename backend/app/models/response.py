from pydantic import BaseModel


class ResponseModel(BaseModel):
    status_code: int
    message: str
    data: dict
    
class CustomResponse:
    def __init__(self, status_code, message, data):
        self.status_code = status_code
        self.message = message
        self.data = data
    def dict(self):
        return {
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data
        }
