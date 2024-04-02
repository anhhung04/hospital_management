from fastapi.responses import JSONResponse, PlainTextResponse


class APIResponse:
    @staticmethod
    def as_json(code: int, message: str, data: dict) -> JSONResponse:
        return JSONResponse(status_code=code, content={
            "status_code": code,
            "message": message,
            "data": data
        })

    @staticmethod
    def as_text(code: int, message: str) -> PlainTextResponse:
        return PlainTextResponse(status_code=code, content=message)
