from fastapi.responses import JSONResponse


def wrap_response(code, message, data):
    return JSONResponse(status_code=code, content={
        "status_code": code,
        "message": message,
        "data": data
    })
