from fastapi import APIRouter

from api.kafka.router import router as kafka_router

router = APIRouter()


router.include_router(kafka_router)
