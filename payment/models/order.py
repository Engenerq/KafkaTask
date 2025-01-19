from pydantic import BaseModel, UUID4


class Order(BaseModel):
    order_uid: UUID4
    user_email: str
