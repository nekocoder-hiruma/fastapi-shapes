from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import User
from app.schemas import UserCreate, UserUpdate
from app.utils import get_password_hashed, verify_password


class UserCRUD(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db_session: Session, *, email:str) -> Optional[User]:
        return db_session.query(User).filter(User.email == email).first()

    def create(self, db_session: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hashed(obj_in.password),
            name=obj_in.name,
            is_administrator=obj_in.is_administrator,
        )
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def authenticate(self, db_session: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db_session, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_administrator(self, user: User) -> bool:
        return user.is_administrator


user = UserCRUD(User)
