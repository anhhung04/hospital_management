from models.response import CustomResponse
from fastapi import status
from fastapi.responses import Response

def wrap_response(code, message, data) -> CustomResponse:
    return Response(
        status_code=code,
        content=CustomResponse(code, message, data).dict()
    )
