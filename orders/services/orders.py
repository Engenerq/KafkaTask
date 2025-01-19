from models.order import Order

from faststream.kafka.publisher.asyncapi import AsyncAPIDefaultPublisher
from fastapi import Request, Depends

from repository.db import OrdersRepository


class ServicesOrder:
    def __init__(self,
                 publisher: AsyncAPIDefaultPublisher,
                 repository: OrdersRepository,
                 ):
        self.publisher = publisher
        self.repository = repository

    @classmethod
    async def create(cls,
                     request: Request,
                     repository: OrdersRepository = Depends(OrdersRepository.create),
                     ):
        app = request.app
        state = app.state
        return cls(
            publisher=state.kafka_topic,
            repository=repository,
        )

    async def create_order(self, order: Order):
        data = await self.repository.create_order(email=order.user_email, status="ORDERED")
        await self.publisher.publish(dict(data))
