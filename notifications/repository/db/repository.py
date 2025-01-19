from asyncpg import Connection
from fastapi import Depends
from uuid import uuid4

from core.dependency.db import _get_connection_from_pool, _get_connection_from_pool_context

from repository.db.sql import CREATE_NOTIFICATION


class NotificationRepository:
    def __init__(self, connection: Connection):
        self._connection = connection

    @classmethod
    async def create(cls, connection: Connection = Depends(_get_connection_from_pool)):
        return cls(
            connection=connection,
        )

    @classmethod
    async def create_fs(cls, connection: Connection = Depends(_get_connection_from_pool_context)):
        return cls(
            connection=connection,
        )

    async def create_notification(self, order_uid: uuid4, email: str, status: str):
        return await self._connection.fetchrow(CREATE_NOTIFICATION, order_uid, email, status)
