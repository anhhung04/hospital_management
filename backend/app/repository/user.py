from repository.schemas.user import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.user import QueryUserModel, PatchUserDetailModel, AddUserDetailModel
from uuid import uuid4
from typing import Tuple, Optional


class UserRepo:
    def __init__(self, session: Session):
        self._session: Session = session

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
        update_item: PatchUserDetailModel
    ) -> Tuple[User, Exception]:
        try:
            user: User = await self.get(query)
            for attr in update_item.model_dump_json().keys():
                if update_item.get(attr) is not None:
                    setattr(user, attr, update_item.get(attr))
            self._session.add(user)
            self._session.commit()
            self._session.refresh(user)
            return user, None
        except Exception as err:
            return None, err

    async def create(
        self,
        user: AddUserDetailModel
    ) -> Tuple[User, Optional[Exception | IntegrityError]]:
        try:
            new_user = user.model_dump_json()
            new_user.update({"id": str(uuid4())})
            new_user = User(**new_user)
            self._session.add(new_user)
            self._session.commit()
            return new_user, None
        except IntegrityError as err:
            return None, err
        except Exception as err:
            return None, err

    async def delete(self, query: QueryUserModel) -> Tuple[User, Exception]:
        try:
            user: User = await self.get(query)
            self._session.delete(user)
            self._session.commit()
            return user, None
        except Exception as e:
            return None, e
