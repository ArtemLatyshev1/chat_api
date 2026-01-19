from fastapi import FastAPI
from app.routers.chats import router as chats_router
from app.routers.messages import router as messages_router

app = FastAPI(title="Chat API")

app.include_router(chats_router)
app.include_router(messages_router)
