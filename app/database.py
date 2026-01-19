import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@db:5432/chat_db"
)
#Создание движка
engine = create_engine(DATABASE_URL)
# Создание сессии
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

#когда сессия заканчивается - БД закрывается,
#FastAPI сам открывает и закрывает соединение для каждого запроса
#Используется для работы с БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


