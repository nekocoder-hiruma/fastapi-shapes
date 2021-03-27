from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN

from app import schemas, crud
from app.database.db import get_db

router = APIRouter()


@router.post("/", response_model=schemas.UserBaseInDB, summary="User Register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.user.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN,
                            detail="User already existed in database")
    return crud.user.create(db_session=db, obj_in=user)
