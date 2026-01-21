from datetime import datetime

#Описание таблиц на Python, таблица Chat
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class Chat(Base):
    __tablename__ = "chats"

    #ID чата
    id = Column(Integer, primary_key=True)
    #название чата
    title = Column(String(200), nullable=False)
    #дата создание чата, используем стандарт UTC чтобы не зависеть от расположения сервера
    created_at = Column(DateTime, default=datetime.utcnow())

    #Связь с таблицей Message, один ко многим, chat.messages - message.chat. Если удалится чат, то все его сообщения удаляются
    messages = relationship(
        "Message",
        back_populates="chat",
        cascade="all, delete"
    )
