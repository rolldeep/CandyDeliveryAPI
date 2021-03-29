from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field


class CourierType(Enum):
    foot = 'foot'
    bike = 'bike'
    car = 'car'

class CourierBase(BaseModel):
    id: int
    courier_type: CourierType

    class Config:
        orm_mode = True


class CourierCreate(CourierBase):
    regions: List[int]
    working_hours: List[str]




class CouriersIds(BaseModel):
    couriers: List[CourierBase]




class CourierGetResponse(BaseModel):
    courier_id: int
    courier_type: CourierType
    regions: List[int]
    working_hours: List[str]
    rating: Optional[float] = None
    earnings: int



class CourierUpdateRequest(BaseModel):
    courier_type: Optional[CourierType] = None
    regions: Optional[List[int]] = None
    working_hours: Optional[List[str]] = None


class OrderItem(BaseModel):
    order_id: int
    weight: float
    region: int
    delivery_hours: List[str]


class Order(BaseModel):
    id: int


class OrdersIds(BaseModel):
    orders: List[Order]


class AssignTime(BaseModel):
    assign_time: Optional[str] = Field(None, example='2021-01-10T09:32:14.42Z')


class OrdersAssignPostRequest(BaseModel):
    courier_id: int


class OrdersCompletePostRequest(BaseModel):
    courier_id: int
    order_id: int
    complete_time: str = Field(..., example='2021-01-10T10:33:01.42Z')


class OrdersCompletePostResponse(BaseModel):
    order_id: int


class CouriersPostRequest(BaseModel):
    data: List[CourierCreate]


class OrdersPostRequest(BaseModel):
    data: List[OrderItem]
