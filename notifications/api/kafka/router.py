from fastapi import Depends
from faststream.kafka.fastapi import KafkaRouter

from core.config import get_settings
from models.shipping import ShippingModel
from services.notification import ServicesNotification

settings = get_settings()

router = KafkaRouter(f"{settings.kafka.host}:{settings.kafka.port}")


@router.subscriber(settings.kafka_topic.sent_orders)
async def notifying(
        msg: ShippingModel,
        service: ServicesNotification = Depends(ServicesNotification.create_fs)
):
    await service.create_notification(msg)
    print(f"Отправили сообщение пользователю: {msg}")
    return
