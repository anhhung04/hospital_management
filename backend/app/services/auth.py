from sqlalchemy.orm import Session
from redis import Redis
from models.user import UserAuth
from typing import Tuple
from util.jwt import create_access_token
from util.crypto import verify_password
from repository.user import get_user_by_username

async def get_access_token(db: Session, redis_client: Redis, user_auth: UserAuth) -> Tuple[str, str]:
    user = await get_user_by_username(db, user_auth.username)
    if redis_client.get(str(user.id)):
        return None, "User already logged in"
    if not verify_password(user.password, user_auth.password, user.username):
        return None, "Invalid username or password"
    access_token, err = create_access_token(redis_client, {"username": user.username}, str(user.id))
    if err:
        return None, err
    return access_token, None