
#Описание таблиц на Python, таблица Message
from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    text = Column(String(5000), nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))

    chat = relationship("Chat", back_populates="messages")
