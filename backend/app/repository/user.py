from repository.schemas.user import User
from util.log import logger

async def get_user_by_username(db, username) -> User:
    try:
        return db.query(User).filter(User.username == username).first()
    except Exception as e:
        logger.error("get_user_by_username error", reason=str(e))
        return None