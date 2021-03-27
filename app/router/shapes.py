from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.database.db import get_db
from app.schemas import TriangleCreateUpdate, SquareCreateUpdate, RectangleCreateUpdate, DiamondCreateUpdate

router = APIRouter()


@router.get("/{item_type}/all/")
def read_shape_list(db: Session = Depends(get_db), item_type: str = "",
                skip: int = 0, limit: int = 100):
    """
    Retrieve list of shapes based on the shape type queried
    """
    item_type = item_type.lower()
    if item_type == "triangle":
        shape_list = crud.triangle.get_multi(db, skip=skip, limit=limit)
    elif item_type == "square":
        shape_list = crud.square.get_multi(db, skip=skip, limit=limit)
    elif item_type == "rectangle":
        shape_list = crud.rectangle.get_multi(db, skip=skip, limit=limit)
    elif item_type == "diamond":
        shape_list = crud.diamond.get_multi(db, skip=skip, limit=limit)
    else:
        raise HTTPException(status_code=400, detail="No such item type")
    return shape_list


@router.get("/{item_type}/get/{item_name}/")
def read_shape(*, db: Session = Depends(get_db), item_type: str, item_name: str):
    item_type = item_type.lower()
    if item_type == "triangle":
        shape = crud.triangle.get_by_name(db, obj_name=item_name)
    elif item_type == "square":
        shape = crud.square.get_by_name(db, obj_name=item_name)
    elif item_type == "rectangle":
        shape = crud.rectangle.get_by_name(db, obj_name=item_name)
    elif item_type == "diamond":
        shape = crud.diamond.get_by_name(db, obj_name=item_name)
    else:
        raise HTTPException(status_code=400, detail="No such item type")
    return shape


@router.post("/{item_type}/create/")
def create_shape(*, db: Session = Depends(get_db), item_type: str,
                 item_in):
    """
    Create the shape based on the shape type queried
    """
    item_type = item_type.lower()
    if item_type == "triangle":
        item_in: TriangleCreateUpdate
        shape = crud.triangle.create(db_session=db, obj_in=item_in)
    elif item_type == "square":
        item_in: SquareCreateUpdate
        shape = crud.square.create(db_session=db, obj_in=item_in)
    elif item_type == "rectangle":
        item_in: RectangleCreateUpdate
        shape = crud.rectangle.create(db_session=db, obj_in=item_in)
    elif item_type == "diamond":
        item_in: DiamondCreateUpdate
        shape = crud.diamond.create(db_session=db, obj_in=item_in)
    else:
        raise HTTPException(status_code=400, detail="No such item type")
    return shape


@router.put("/{item_type}/update/{item_id}/")
def update_shape(*, db: Session = Depends(get_db), item_type: str, item_id: int, item_in):
    """
    Update the shape based on the shape type and shape id queried
    """
    item_type = item_type.lower()
    if item_type == "triangle":
        item_in: TriangleCreateUpdate
        shape = crud.triangle.get(db_session=db, obj_id=item_id)
        if not shape:
            raise HTTPException(status_code=404, detail=f"{item_type} not found")
        shape = crud.triangle.update(db_session=db, db_obj=shape, obj_in=item_in)
    elif item_type == "square":
        item_in: SquareCreateUpdate
        shape = crud.square.get(db_session=db, obj_id=item_id)
        if not shape:
            raise HTTPException(status_code=404, detail=f"{item_type} not found")
        shape = crud.square.update(db_session=db, db_obj=shape, obj_in=item_in)
    elif item_type == "rectangle":
        item_in: RectangleCreateUpdate
        shape = crud.rectangle.get(db_session=db, obj_id=item_id)
        if not shape:
            raise HTTPException(status_code=404, detail=f"{item_type} not found")
        shape = crud.rectangle.update(db_session=db, db_obj=shape, obj_in=item_in)
    elif item_type == "diamond":
        item_in: DiamondCreateUpdate
        shape = crud.diamond.get(db_session=db, obj_id=item_id)
        if not shape:
            raise HTTPException(status_code=404, detail=f"{item_type} not found")
        shape = crud.diamond.update(db_session=db, db_obj=shape, obj_in=item_in)
    else:
        raise HTTPException(status_code=400, detail="No such item type")
    return shape
