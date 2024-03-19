from fastapi import APIRouter, HTTPException
from models.user import UserAuth
from util.crypto import password_context
from util.response import wrap_respponse, status
from util.jwt import create_access_token
from repository.schemas.user import User as UserInDB
from repository import get_db

router = APIRouter()

@router.post("/login")
async def login(user_auth: UserAuth):
    db = get_db()
    try: 
        user: UserInDB = db.query(UserInDB).filter(UserInDB.username == user_auth.username).first()
    except Exception:
        return wrap_respponse(status.HTTP_404_NOT_FOUND, "User not found", {})
    if not password_context.verify("password", user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect username or password",
        )
    access_token: str = create_access_token(user.id)
    return wrap_respponse(status.HTTP_200_OK, "login successful", {"access_token": access_token})