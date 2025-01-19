from fastapi import Depends

from models.shipping import ShippingModel
from repository.db import NotificationRepository


class ServicesNotification:
    def __init__(self,
                 repository: NotificationRepository,
                 ):
        self.repository = repository

    @classmethod
    async def create(cls,
                     repository: NotificationRepository = Depends(NotificationRepository.create),
                     ):
        return cls(
            repository=repository,
        )

    @classmethod
    async def create_fs(cls,
                        repository: NotificationRepository = Depends(NotificationRepository.create_fs),
                        ):
        return cls(
            repository=repository,
        )

    async def create_notification(self, shipping: ShippingModel):
        await self.repository.create_notification(order_uid=shipping.order_uid, email=shipping.user_email,
                                                  status="SHIPPED")
