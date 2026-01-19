from pydantic import BaseModel, constr
from datetime import datetime


class MessageCreate(BaseModel):
    text: constr(min_length=1, max_length=5000)


class MessageOut(BaseModel):
    id: int
    text: str
    created_at: datetime

    class Config:
        orm_mode = True

