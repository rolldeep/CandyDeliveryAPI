from sqlalchemy.orm import Session



from app.models import courier, courier_type, shift
from app.shemas import shemas




def get_courier(db: Session, courier_id: int):

    return db.query(courier.Courier).filter(courier.Courier.id == courier_id).first()



def get_couriers(db: Session, skip: int = 0, limit: int = 100):

    return db.query(courier.Courier).offset(skip).limit(limit).all()



def create_courier(db: Session, courier: shemas.CourierCreate, shifts):
    db_courier = courier.Courier(regions=courier.regions,
                                 working_hours=courier.working_hours,
                                 type=courier.courier_type)
    db.add(db_courier)
    db.commit()
    db.refresh(db_courier)
    return db_courier



def get_items(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Item).offset(skip).limit(limit).all()



def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
