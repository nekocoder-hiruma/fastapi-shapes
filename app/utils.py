from datetime import timedelta, datetime

import jwt
from fastapi import Depends, Security, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN

from app import config, crud
from app.config import SECRET_KEY, ALGORITHM
from app.database.db import db_session, get_db
from app.schemas import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{config.API_PREFIX}/login/token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hashed(password):
    return pwd_context.hash(password)


def authenticate_user(db: db_session, email: str, password: str):
    user = crud.user.get_by_email(db_session=db, email=email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(db: Session = Depends(get_db), token: str = Security(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenData(**payload)
    except PyJWTError:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    user = crud.user.get(db, obj_id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
