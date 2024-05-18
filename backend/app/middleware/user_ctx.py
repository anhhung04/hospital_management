from util.jwt import JWTHandler
from fastapi import Depends
from typing import Annotated
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

securityHeader = HTTPBearer(
    scheme_name="Bearer", auto_error=False
)

class UserContext:
    def __init__(
        self,
        token: Annotated[HTTPAuthorizationCredentials, Depends(securityHeader)],
        jwt_handler: JWTHandler = Depends(JWTHandler)
    ):
        try:
            if token is None:
                self._info = {}
            else:
                token_data = jwt_handler.verify(token.credentials)
                self._info = token_data
        except Exception:
            self._info = {}

    def role(self):
        return self._info.get('info', {}).get('role', None)

    def id(self):
        return self._info.get('sub', None)
