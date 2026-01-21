from pydantic import BaseModel, constr
from datetime import datetime

#При создании приложения
class MessageCreate(BaseModel):
    text: constr(min_length=1, max_length=5000)

#ответ API
class MessageOut(BaseModel):
    id: int
    text: str
    created_at: datetime

    # orm_mode позволяет Pydantic работать напрямую с ORM-объектами
    class Config:
        orm_mode = True

