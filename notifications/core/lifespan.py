from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI
from faststream.utils.context.repository import context

from core.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    app.state.db_pool = pool = await asyncpg.create_pool(
        dsn=str(settings.postgres.dsn),
        min_size=1,
        max_size=10,
    )

    context.set_global("db_pool", pool)

    yield

    await pool.close()
