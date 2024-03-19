from fastapi.responses import JSONResponse
from fastapi import status


def wrap_respponse(code, message, data):
    return JSONResponse(status_code=code, content={"status_code": code, "message": message, "data": data})