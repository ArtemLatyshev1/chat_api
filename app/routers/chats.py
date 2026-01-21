from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Chat, Message
from app.schemas.chat import ChatCreate, ChatOut
from app.schemas.message import MessageCreate

router = APIRouter()


@router.post("/chats/")
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    new_chat = Chat(title=chat.title.strip())
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat


@router.post("/chats/{chat_id}/messages/")
def create_message(chat_id: int, msg: MessageCreate, db: Session = Depends(get_db)):
    #получаем только сообщения этого чата
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    message = Message(text=msg.text.strip(), chat_id=chat_id)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


@router.get("/chats/{chat_id}")
def get_chat(chat_id: int, limit: int = 20, db: Session = Depends(get_db)):
    limit = min(limit, 100)
    #получаем только сообщения этого чата
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    messages = (
        #Сообщения из базы только от этого чата, берем последние сообщения сортировкой по убыванию,
        # по умолчанию - 20 сообщений, максимум - 100
        db.query(Message)
        .filter(Message.chat_id == chat_id)
        .order_by(Message.created_at.desc())
        .limit(limit)
        .all()
    )

    return {
        "id": chat.id,
        "title": chat.title,
        "created_at": chat.created_at,
        "messages": list(reversed(messages)),
    }


@router.delete("/chats/{chat_id}", status_code=204)
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404)

    db.delete(chat)
    db.commit()


@router.get("/chats/", response_model=list[ChatOut])
def get_chats(db: Session = Depends(get_db)):
    return db.query(Chat).all()
