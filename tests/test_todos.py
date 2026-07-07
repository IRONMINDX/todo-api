from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_create_todo():
    response = client.post("/todos", json={"title": "Test Todo",
                                        "description": "This is a test todo",
                                        "status": "pending",
                                        "priority": "high",
                                        "user_id":"85dc421f-d43c-46d5-a76e-054b13494ebd"
                                        })
    assert response.status_code in [200, 201]
    assert response.json()["title"] == "Test Todo"


def test_update_todo():
    response = client.put("/todos/a07fa2f6-6feb-4554-9a8b-8fc4fb801513", json={"title": "Updated Test Todo",
                                        "description": "This is an updated test todo",
                                        "status": "completed",
                                        "priority": "low",
                                        "user_id":"85dc421f-d43c-46d5-a76e-054b13494ebd"
                                        })
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Todo"

def delete_todo():
    response = client.delete("/todos/a07fa2f6-6feb-4554-9a8b-8fc4fb801513")
    assert response.status_code == 200

def search_todo():
    response = client.get("/todos/search?query=Test")
    assert response.status_code == 200

def test_pagination():
    response = client.get("/todos?page=1&size=10")
    assert response.status_code == 200
    


def test_validation():
    response = client.get("/todos?page=0")
    assert response.status_code == 400
    assert response.json()["success"] is False