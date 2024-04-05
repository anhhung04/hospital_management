from models.request import AUTH_HEADER
from util.jwt import JWTHandler
from fastapi import Request, Depends


class UserContext:
    def __init__(self, request: Request, jwt_handler: JWTHandler = Depends(JWTHandler)):
        auth_header = request.headers.get(AUTH_HEADER, None)
        token = auth_header.split(" ")[-1] if auth_header else None
        try:
            if auth_header is None:
                self._info = {}
            else:
                token_data = jwt_handler.verify(token)
                self._info = token_data
        except Exception:
            self._info = {}

    def role(self):
        return self._info.get('info', {}).get('role', None)

    def id(self):
        return self._info.get('sub', None)
