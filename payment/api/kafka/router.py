from faststream.kafka.fastapi import KafkaRouter
from fastapi import Depends

from models.order import Order
from models.pay import Payment
from core.config import get_settings
from services.payment import ServicesPayment


settings = get_settings()

router = KafkaRouter(f"{settings.kafka.host}:{settings.kafka.port}")


@router.subscriber(settings.kafka_topic.order)
@router.publisher(settings.kafka_topic.payed)
async def payment(
        msg: Order,
        service: ServicesPayment = Depends(ServicesPayment.create_fs)
):
    await service.create_payment(msg)
    return Payment(**msg.model_dump())
