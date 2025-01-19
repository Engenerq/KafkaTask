from pydantic import BaseModel, UUID4


class ShippingModel(BaseModel):
    order_uid: UUID4
    user_email: str
    status: str = "shipped"
