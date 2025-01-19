from collections.abc import AsyncGenerator
from typing import Annotated

from asyncpg import Connection, Pool
from fastapi import Request
from faststream.kafka.fastapi import Context


async def _get_connection_from_pool(request: Request) -> AsyncGenerator[Connection, None]:
    pool: Pool = request.app.state.db_pool
    async with pool.acquire() as conn:
        yield conn


async def _get_connection_from_pool_context(db_pool: Annotated[Pool, Context("db_pool")]) -> AsyncGenerator[Connection, None]:
    async with db_pool.acquire() as conn:
        yield conn
