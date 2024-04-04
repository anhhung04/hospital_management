from repository.schemas.user import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from collections import namedtuple
from uuid import uuid4
from typing import Tuple, Optional

GetUserQuery = namedtuple('GetUserQuery', ['id', 'username'])


class UserRepo:
    def __init__(self, session: Session):
        self._session: Session = session

    async def get(self, query: GetUserQuery) -> Tuple[User, Exception]:
        try:
            if query.username:
                user = self._session.query(User).filter(
                    User.username == query.username).first()
            if query.id:
                user = self._session.query(User).filter(
                    User.id == query.id).first()
            return user, None
        except Exception as err:
            return None, err

    async def update(self, query: GetUserQuery, update_item: dict) -> Tuple[User, Exception]:
        try:
            user: User = await self.get(query)
            if user:
                for attr in update_item.keys():
                    setattr(user, attr, update_item[attr])
                self._session.add(user)
                self._session.commit()
                self._session.refresh(user)
            return user, None
        except Exception as err:
            return None, err

    async def create(self, item: dict) -> Tuple[User, Optional[Exception | IntegrityError]]:
        try:
            item.update({'id': str(uuid4())})
            new_user = User(**item)
            self._session.add(new_user)
            self._session.commit()
            return new_user, None
        except IntegrityError as err:
            return None, err
        except Exception as err:
            return None, err

    async def delete(self, query: GetUserQuery) -> Tuple[User, Exception]:
        try:
            user: User = await self.get(query)
            if user:
                self._session.delete(user)
                self._session.commit()
            return user, None
        except Exception as e:
            return None, e
