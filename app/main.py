from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Depends, Query

import uvicorn
from app.shemas.shemas import (
    CourierGetResponse,
    CourierCreate,
    CouriersIds,
    CourierBase,
    CouriersPostRequest,
    CourierUpdateRequest,
    OrdersAssignPostRequest,
    OrdersCompletePostRequest,
    OrdersCompletePostResponse,
    Order,
    OrdersIds,
    OrdersPostRequest,
)

app = FastAPI(
    title='Candy Delivery App',
    version='1.0',
)


@app.post('/couriers', response_model=CouriersIds)
def post_couriers(body: CouriersPostRequest = Depends()) -> CouriersIds:
    data = body.data
    return CouriersIds(couriers=
                       [CourierBase(id=item.courier_id) for item in data])


@app.get('/couriers/{courier_id}', response_model=CourierGetResponse)
def get_couriers_courier_id(courier_id: int = Query(None)) -> CourierGetResponse:

    return courier_id


@app.patch('/couriers/{courier_id}', response_model=Any)
def patch_couriers_courier_id(
        courier_id: int, body: CourierUpdateRequest = None
) -> CourierCreate:
    pass


@app.post('/orders', response_model=OrdersIds)
def post_orders(body: OrdersPostRequest = None) -> OrdersIds:
    data = body.data
    return OrdersIds(orders=
                     [Order(id=item.order_id) for item in data])


@app.post('/orders/assign', response_model=CourierBase)
def post_orders_assign(body: OrdersAssignPostRequest = None) -> CourierBase:
    courier = get_courier(body.courier_id)
    order = get_order(body.order_id)
    return CourierBase


@app.post('/orders/complete', response_model=OrdersCompletePostResponse)
def post_orders_complete(
        body: OrdersCompletePostRequest = None,
) -> OrdersCompletePostResponse:
    pass


if __name__ == '__main__':
    uvicorn.run(app)
