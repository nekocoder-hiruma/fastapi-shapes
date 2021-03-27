from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Triangle, Rectangle, Square, Diamond
from app.schemas import TriangleCreateUpdate, RectangleCreateUpdate, SquareCreateUpdate, DiamondCreateUpdate


class TriangleCRUD(CRUDBase[Triangle, TriangleCreateUpdate, TriangleCreateUpdate]):
    def get_by_name(self, db_session: Session, obj_name: str) -> Optional[Triangle]:
        return db_session.query(self.model).filter(self.model.name == obj_name).first()


triangle = TriangleCRUD(Triangle)


class RectangleCRUD(CRUDBase[Rectangle, RectangleCreateUpdate, RectangleCreateUpdate]):
    def get_by_name(self, db_session: Session, obj_name: str) -> Optional[Rectangle]:
        return db_session.query(self.model).filter(self.model.name == obj_name).first()


rectangle = RectangleCRUD(Rectangle)


class SquareCRUD(CRUDBase[Square, SquareCreateUpdate, SquareCreateUpdate]):
    def get_by_name(self, db_session: Session, obj_name: str) -> Optional[Square]:
        return db_session.query(self.model).filter(self.model.name == obj_name).first()


square = SquareCRUD(Square)


class DiamondCRUD(CRUDBase[Diamond, DiamondCreateUpdate, DiamondCreateUpdate]):
    def get_by_name(self, db_session: Session, obj_name: str) -> Optional[Diamond]:
        return db_session.query(self.model).filter(self.model.name == obj_name).first()


diamond = DiamondCRUD(Diamond)
