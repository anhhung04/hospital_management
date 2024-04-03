from fastapi.responses import JSONResponse, PlainTextResponse


class APIResponse:
    @staticmethod
    def as_json(code: int, message: str, data: dict = {}) -> JSONResponse:
        content = {
            "status_code": code,
            "message": message,
        }
        if data:
            content.update({"data": data})
        return JSONResponse(status_code=code, content=content)

    @staticmethod
    def as_text(code: int, message: str) -> PlainTextResponse:
        return PlainTextResponse(status_code=code, content=message)
