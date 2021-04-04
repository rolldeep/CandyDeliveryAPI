from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from .courier import Courier

class Shift(Base):
    id = Column(Integer, primary_key=True, index=True)
    courier_id = Column(Integer, ForeignKey("user.id"), index=True, nullable=True)
    working_hours = Column(String, index=True, nullable=True)
    courier = relationship("Courier", back_populates="working_hours")
