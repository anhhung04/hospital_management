from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import UserAuth
from util.crypto import verify_password
from util.response import wrap_response, status
from util.jwt import create_access_token
from repository.schemas.user import User as UserInDB
from repository import get_db, get_redis

router = APIRouter()


@router.post("/login")
async def login(user_auth: UserAuth, db: Session = Depends(get_db), redis_client=Depends(get_redis)):
    try: 
        user: UserInDB = db.query(UserInDB).filter(UserInDB.username == user_auth.username).first()
    except Exception:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR, "query database error")
    if not user or not verify_password(user.password, user_auth.password, user.username):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect username or password",
        )
    try:
        access_token, err = create_access_token(redis_client, {
            "username": user.username,
        }, str(user.id))
        if err:
            raise Exception
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="create access token error",
        )
    return wrap_response(status.HTTP_200_OK, "login successful", {"access_token": access_token})