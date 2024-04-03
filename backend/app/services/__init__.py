from sqlalchemy.orm import Session
from redis import Redis


class IService:
    def __init__(self, session: Session, redis_client: Redis, user: dict) -> None:
        self._sess = session
        self._rc = redis_client
        self._current_user = user
