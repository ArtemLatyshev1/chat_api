def test_create_message(client):
    # 1. Создаём чат
    chat = client.post(
        "/chats/",
        json={"title": "Chat for messages"}
    ).json()

    # 2. Создаём сообщение
    response = client.post(
        f"/chats/{chat['id']}/messages/",
        json={"text": "Hello world"}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["text"] == "Hello world"
    assert data["chat_id"] == chat["id"]


def test_get_messages(client):
    chat = client.post(
        "/chats/",
        json={"title": "Chat with history"}
    ).json()

    client.post(
        f"/chats/{chat['id']}/messages/",
        json={"text": "First message"}
    )

    response = client.get(f"/chats/{chat['id']}/messages/")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
