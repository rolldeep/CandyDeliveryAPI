from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from .courier import Courier

class CourierType(Base):
    type = Column(String, index=True, nullable=True)
    id = Column(Integer, ForeignKey("courier.type"), index=True)