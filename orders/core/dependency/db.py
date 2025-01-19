from collections.abc import AsyncGenerator

from asyncpg import Connection, Pool
from fastapi import Request


async def _get_connection_from_pool(request: Request) -> AsyncGenerator[Connection, None]:
    pool: Pool = request.app.state.db_pool
    async with pool.acquire() as conn:
        yield conn
