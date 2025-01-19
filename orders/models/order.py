from pydantic import BaseModel


class Order(BaseModel):
    user_email: str
