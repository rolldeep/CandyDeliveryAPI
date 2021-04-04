# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  
from app.models.item import Item  
from app.models.user import User  
from app.models.courier import Courier
from app.models.courier_type import CourierType
from app.models.shift import Shift
