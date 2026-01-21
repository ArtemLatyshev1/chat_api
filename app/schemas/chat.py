
# Валидация входных данных
from pydantic import BaseModel, constr
from datetime import datetime

#Название чата, при его создании, должно быть не пустым и не больше 200 символов. Входные данные
class ChatCreate(BaseModel):
    title: constr(min_length=1, max_length=200)

#Схема ответа API
class ChatOut(BaseModel):
    id: int
    title: str
    created_at: datetime

    #orm_mode позволяет Pydantic работать напрямую с ORM-объектами
    class Config:
        orm_mode = True
