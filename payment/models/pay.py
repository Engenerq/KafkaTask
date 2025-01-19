from pydantic import BaseModel, UUID4


class Payment(BaseModel):
    order_uid: UUID4
    user_email: str
    status: str = "payed"
