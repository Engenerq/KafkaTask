from pydantic import BaseModel, UUID4


class PayOk(BaseModel):
    order_uid: UUID4
    user_email: str
    status: str = "ok"
