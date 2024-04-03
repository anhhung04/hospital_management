from repository.schemas.user import User
from util.log import logger
from repository import IRepo
from sqlalchemy.orm import Session
from collections import namedtuple
from uuid import uuid4

GetUserQuery = namedtuple('GetUserQuery', ['id', 'username'])


class UserRepo(IRepo):
    def __init__(self, session: Session):
        self._session: Session = session

    async def get(self, query: GetUserQuery):
        try:
            if query.username:
                user = self._session.query(User).filter(
                    User.username == query.username).first()
            if query.id:
                user = self._session.query(User).filter(
                    User.id == query.id).first()
            return user
        except Exception as e:
            logger.error(e)
            return None

    async def update(self, query: GetUserQuery, update_item: dict) -> User:
        try:
            user: User = await self.get(query)
            if user:
                for attr in update_item.keys():
                    setattr(user, attr, update_item[attr])
                self._session.add(user)
                self._session.commit()
                self._session.refresh(user)
            return user
        except Exception as e:
            logger.error(e)
            return None

    async def create(self, item: dict) -> User:
        try:
            item.update({'id': str(uuid4())})
            new_user = User(**item)
            self._session.add(new_user)
            self._session.commit()
            return new_user
        except Exception as e:
            logger.error(e)
            return None

    async def delete(self, query: GetUserQuery) -> User:
        try:
            user: User = await self.get(query)
            if user:
                self._session.delete(user)
                self._session.commit()
            return user
        except Exception as e:
            logger.error(e)
            return None
