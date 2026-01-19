# Chat API (Test Task)

Небольшое API для работы с чатами и сообщениями.

## Описание

Приложение позволяет:

* создавать чаты
* отправлять сообщения в чат
* получать чат с последними сообщениями
* удалять чат вместе со всеми сообщениями

Проект написан с использованием **FastAPI**, **PostgreSQL**, **SQLAlchemy** и запускается через **Docker**.

---

## Используемые технологии

* Python 3.12
* FastAPI
* SQLAlchemy (ORM)
* PostgreSQL
* Alembic (миграции)
* pytest (тесты)
* Docker, docker-compose

---

## Структура проекта

```
chat_api/
├── app/
│   ├── main.py              # точка входа
│   ├── database.py          # подключение к БД
│   ├── models/              # SQLAlchemy модели
│   ├── schemas/             # Pydantic схемы
│   ├── routers/             # API роутеры
│   └── crud/                # работа с БД
├── alembic/                 # миграции
├── tests/                   # pytest тесты
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Запуск проекта

### 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd chat_api
```

### 2. Запустить через Docker

```bash
docker compose up --build
```

После запуска:

* API доступно по адресу:
  **[http://localhost:8000](http://localhost:8000)**
* Swagger UI:
  **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## Миграции базы данных

Миграции выполняются автоматически при первом запуске контейнеров.

При необходимости можно выполнить вручную:

```bash
docker compose exec web alembic upgrade head
```

---

## API эндпоинты

### Создать чат

```
POST /chats/
Body: { "title": "Chat title" }
```

### Отправить сообщение

```
POST /chats/{id}/messages/
Body: { "text": "Message text" }
```

### Получить чат с сообщениями

```
GET /chats/{id}?limit=20
```

### Удалить чат

```
DELETE /chats/{id}
```

---

## Тесты

Для запуска тестов:

```bash
docker compose exec web pytest
```

Тесты покрывают:

* создание чатов
* получение чатов
* отправку сообщений
* получение сообщений

---

## Примечания

Проект включает базовую архитектуру, был сделан
акцент на читаемость и понятность кода

---

## Автор

Артём Латышев
