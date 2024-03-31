from repository.schemas.user import User
from util.log import logger
from repository import IRepo
from sqlalchemy.orm import Session
from repository.schemas.user import User
from collections import namedtuple

GetUserQuery = namedtuple('GetUserQuery', ['id', 'username'])


class UserRepo(IRepo):
    def __init__(self, session: Session):
        self._session: Session = session

    def get(self, query: GetUserQuery) -> User:
        try:
            if query.id:
                return self._session.query(User).filter(User.id == query.id).first()
            return self._session.query(User).filter(User.username == query.username).first()
        except Exception as e:
            logger.error(e)
            return None

    def update(self, query: GetUserQuery, update_item: User) -> User:
        try:
            user: User = self.get(query)
            if user:
                for key, value in update_item.dict().items():
                    setattr(user, key, value)
                self._session.commit()
            return user
        except Exception as e:
            logger.error(e)
            return None

    def create(self, item: User) -> User:
        try:
            self._session.add(item)
            self._session.commit()
            return item
        except Exception as e:
            logger.error(e)
            return None

    def delete(self, query: GetUserQuery) -> User:
        try:
            user: User = self.get(query)
            if user:
                self._session.delete(user)
                self._session.commit()
            return user
        except Exception as e:
            logger.error(e)
            return None
