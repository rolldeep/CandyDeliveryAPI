from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Courier(Base):
    id = Column(Integer, primary_key=True, index=True)
    regions = Column(String, index=True)
    rating = Column(Float)
    earnings = Column(Float, default=True)
    working_hours = relationship("Shift", back_populates="courier")
    type = relationship("CourierType", back_populates="id")
