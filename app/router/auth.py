from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from app import crud
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.database.db import get_db
from app.schemas import Token
from app.utils import create_access_token

router = APIRouter()


@router.post("/login/", response_model=Token, summary="User Login for access token",
             tags=["login"])
async def login_for_access_token(db: Session = Depends(get_db),
                                 form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.user.authenticate(db_session=db,
                                  email=form_data.username,
                                  password=form_data.password)
    if not user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"email": user.email,
                                             "user_id": user.id},
                                       expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
