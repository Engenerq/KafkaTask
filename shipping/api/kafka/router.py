from fastapi import Depends
from faststream.kafka.fastapi import KafkaRouter

from models.pay import PayOk

from core.config import get_settings
from models.shipping import ShippingModel

from services.shiping import ServicesShipping

settings = get_settings()

router = KafkaRouter(f"{settings.kafka.host}:{settings.kafka.port}")


@router.subscriber(settings.kafka_topic.payed)
@router.publisher(settings.kafka_topic.sent_orders)
async def shipping(
        msg: PayOk,
        service: ServicesShipping = Depends(ServicesShipping.create_fs)
):
    await service.create_shipping(msg)
    return ShippingModel(
        order_uid=msg.order_uid,
        user_email=msg.user_email,
        status="shipped",
    )
