from models.order import Order

from fastapi import Depends


from repository.db import PaymentRepository


class ServicesPayment:
    def __init__(self,
                 repository: PaymentRepository,
                 ):
        self.repository = repository

    @classmethod
    async def create(cls,
                     repository: PaymentRepository = Depends(PaymentRepository.create),
                     ):
        return cls(
            repository=repository,
        )

    @classmethod
    async def create_fs(cls,
                        repository: PaymentRepository = Depends(PaymentRepository.create_fs),
                        ):
        return cls(
            repository=repository,
        )

    async def create_payment(self, order: Order):
        await self.repository.create_payment(order_uid=order.order_uid, email=order.user_email, status="PAYED")
