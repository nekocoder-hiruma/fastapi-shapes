from sqlalchemy import Column, Integer, String

from app.database import Base


class BaseModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
