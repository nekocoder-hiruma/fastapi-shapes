from sqlalchemy import Column, String, Boolean

from app.models.base import BaseModel


class User(BaseModel):
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_administrator = Column(Boolean, default=False)
