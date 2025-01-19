from contextlib import asynccontextmanager

from fastapi import FastAPI
from faststream.kafka import KafkaBroker
import asyncpg

from core.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    kafka_settings = settings.kafka
    topic = settings.kafka_topic
    broker = KafkaBroker(f"{kafka_settings.host}:{kafka_settings.port}")
    await broker.start()
    app.state.kafka = broker
    app.state.kafka_topic = broker.publisher(topic.order)
    app.state.db_pool = pool = await asyncpg.create_pool(
        dsn=str(settings.postgres.dsn),
        min_size=1,
        max_size=10,
    )

    yield
    await broker.close()
    await pool.close()
