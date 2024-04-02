from models.request import AUTH_HEADER
from util.jwt import JWTHandler
from repository import RedisStorage
from fastapi import Request, Depends, HTTPException


async def auth_middleware(request: Request, rc=Depends(RedisStorage.get)):
    auth_header = request.headers.get(AUTH_HEADER, None)
    token = auth_header.split(" ")[-1] if auth_header else None
    try:
        if auth_header is None:
            request.state.user = None
        else:
            token_data, err = JWTHandler(rc).verify(token)
            if err:
                raise HTTPException(status_code=401, detail=str(err))
            request.state.user = token_data.get('info', None)
            request.state.user.update({'sub': token_data.get('sub')})
    except Exception:
        request.state.user = None


async def get_current_user(request: Request):
    return request.state.user