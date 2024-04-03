class IService:
    def __init__(self, session=None, user: dict = None, redis_client=None) -> None:
        self._sess = session
        self._rc = redis_client
        self._current_user = user
