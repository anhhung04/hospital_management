from repository.schemas.user import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.user import QueryUserModel, PatchUserDetailModel, AddUserDetailModel
from typing import Tuple, Optional
from fastapi import Depends
from repository import Storage


class UserRepo:
    def __init__(self, session: Session = Depends(Storage.get)):
        self._session: Session = session

    @staticmethod
    async def call():
        return UserRepo()

    async def get(
        self,
        query: QueryUserModel
    ) -> Tuple[User, Exception]:
        try:
            user = self._session.query(User).filter(
                User.id == query.id if query.id else None
                or User.username == query.username if query.username else None
                or User.email == query.email if query.email else None
                or User.ssn == query.ssn if query.ssn else None
            ).first()
            return user, None
        except Exception as err:
            return None, err

    async def update(
        self,
        query: QueryUserModel,
        update_user: PatchUserDetailModel
    ) -> Tuple[User, Exception]:
        try:
            user, err = await self.get(query)
            if err:
                return None, err
            dump_update_user = update_user.model_dump()
            for attr in dump_update_user.keys():
                if dump_update_user.get(attr) is not None:
                    setattr(user, attr, dump_update_user.get(attr))
            self._session.add(user)
            self._session.commit()
            self._session.refresh(user)
            return user, None
        except Exception as err:
            self._session.rollback()
            return None, err

    async def create(
        self,
        user: AddUserDetailModel
    ) -> Tuple[User, Optional[Exception | IntegrityError]]:
        try:
            new_user = user.model_dump()
            new_user = User(**new_user)
            self._session.add(new_user)
            self._session.commit()
            return new_user, None
        except IntegrityError as err:
            self._session.rollback()
            return None, err
        except Exception as err:
            return None, err

    async def delete(self, query: QueryUserModel) -> Tuple[User, Exception]:
        try:
            user, err = await self.get(query)
            if err:
                return None, err
            self._session.delete(user)
            self._session.commit()
            return user, None
        except Exception as e:
            self._session.rollback()
            return None, e
