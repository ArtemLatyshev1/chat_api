def test_create_chat(client):
    response = client.post(
        "/chats/",
        json={"title": "Test chat"}
    )

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["title"] == "Test chat"


def test_get_chats(client):
    response = client.get("/chats/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
