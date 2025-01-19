from asyncpg import Connection
from fastapi import Depends

from core.dependency.db import _get_connection_from_pool
from repository.db.sql import CREATE_ORDER


class OrdersRepository:
    def __init__(self, connection: Connection):
        self._connection = connection

    @classmethod
    async def create(cls, connection: Connection = Depends(_get_connection_from_pool)):
        return cls(
            connection=connection,
        )

    async def create_order(self, email: str, status: str):
        return await self._connection.fetchrow(CREATE_ORDER, email, status)
