from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.chat import Chat
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageOut

router = APIRouter()


@router.post(
    "/chats/{chat_id}/messages/",
    response_model=MessageOut
)
def create_message(
    chat_id: int,
    message: MessageCreate,
    db: Session = Depends(get_db),
):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    msg = Message(
        text=message.text,
        chat_id=chat_id
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


@router.get(
    "/chats/{chat_id}/messages/",
    response_model=list[MessageOut]
)
def get_messages(
    chat_id: int,
    db: Session = Depends(get_db),
    limit: int = 50,
):
    return (
        db.query(Message)
        .filter(Message.chat_id == chat_id)
        .order_by(Message.created_at.asc())
        .limit(limit)
        .all()
    )
