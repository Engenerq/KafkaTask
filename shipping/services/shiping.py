from fastapi import Depends

from models.pay import PayOk
from repository.db import ShippingRepository


class ServicesShipping:
    def __init__(self,
                 repository: ShippingRepository,
                 ):
        self.repository = repository

    @classmethod
    async def create(cls,
                     repository: ShippingRepository = Depends(ShippingRepository.create),
                     ):
        return cls(
            repository=repository,
        )

    @classmethod
    async def create_fs(cls,
                        repository: ShippingRepository = Depends(ShippingRepository.create_fs),
                        ):
        return cls(
            repository=repository,
        )

    async def create_shipping(self, payment: PayOk):
        await self.repository.create_shipping(order_uid=payment.order_uid, email=payment.user_email, status="SHIPPED")
