from sqlalchemy.orm import Session
from redis import Redis


class IService:
    def __init__(self, session: Session = None, redis_client: Redis = None, user: dict = None) -> None:
        self._sess = session
        self._rc = redis_client
        self._current_user = user
