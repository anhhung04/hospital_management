from models.response import CustomResponse
from fastapi import status

def wrap_response(code, message, data) -> CustomResponse:
    return CustomResponse(status_code=code, message=message, data=data)