from pydantic import BaseModel as Base


class BaseSchema(Base):
    name: str


class TriangleBase(BaseSchema):
    base: int
    adjacent: int
    opposite: int


class TriangleCreateUpdate(TriangleBase):
    pass


class Triangle(TriangleBase):
    id: int

    class Config:
        orm_mode = True


class RectangleBase(BaseSchema):
    width: int
    height: int


class RectangleCreateUpdate(RectangleBase):
    pass


class Rectangle(RectangleBase):
    id: int

    class Config:
        orm_mode = True


class SquareBase(BaseSchema):
    side: int


class SquareCreateUpdate(SquareBase):
    pass


class Square(SquareBase):
    id: int

    class Config:
        orm_mode = True


class DiamondBase(BaseSchema):
    length: int
    diagonal_one: int
    diagonal_two: int


class DiamondCreateUpdate(DiamondBase):
    pass


class Diamond(DiamondBase):
    id: int

    class Config:
        orm_mode = True


# User
class UserBase(BaseSchema):
    email: str
    is_administrator: bool = False


class UserBaseInDB(UserBase):
    id: int = None

    class Config:
        orm_mode = True


class UserInDb(UserBaseInDB):
    hashed_password: str


class UserCreate(UserBaseInDB):
    email: str
    password: str


class UserUpdate(UserBaseInDB):
    email: str = None
    name: str = None


# Auth Tokens
class Token(Base):
    access_token: str
    token_type: str


class TokenData(Base):
    email: str = None
    user_id: int = None
