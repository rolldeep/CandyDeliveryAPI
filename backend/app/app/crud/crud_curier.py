from models import courier
from typing import List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.courier import Courier
from app.models.courier_type import CourierType
from app.models.shift import Shift
from app.shemas import shemas


class CRUDCurier(CRUDBase):
    def get_courier(db: Session, courier_id: int) -> Courier:

        return db.query(courier.Courier).filter(courier.Courier.id == courier_id).first()

    def get_couriers(db: Session, skip: int = 0, limit: int = 100) -> List[Courier]:

        return db.query(courier.Courier).offset(skip).limit(limit).all()

    def create_courier(db: Session, courier: shemas.CourierCreate) -> Courier:
        db_courier = courier.Courier(regions=courier.regions,
                                     working_hours=courier.working_hours,
                                     type=courier.courier_type)
        db.add(db_courier)
        db.commit()
        db.refresh(db_courier)
        return db_courier

    # def get_items(db: Session, skip: int = 0, limit: int = 100):

    #     return db.query(models.Item).offset(skip).limit(limit).all()

    # def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    #     db_item = models.Item(**item.dict(), owner_id=user_id)
    #     db.add(db_item)
    #     db.commit()
    #     db.refresh(db_item)
    #     return db_item
courier = CRUDCurier(Courier)