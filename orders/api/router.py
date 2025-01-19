from fastapi import APIRouter, Depends, BackgroundTasks

from models.order import Order
from services.orders import ServicesOrder

router = APIRouter()


@router.get(
    path="/orders",
)
async def get_orders(
        background_tasks: BackgroundTasks,
        data: Order = Depends(),
        service: ServicesOrder = Depends(ServicesOrder.create),
):
    await service.create_order(data)
    # background_tasks.add_task(service.create_order, data)
    return {"success": True}
