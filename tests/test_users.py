from fastapi.testclient import TestClient
from app.main import app
from app import schemas

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.json().get("message") == "Welcome to fastAPI"
    assert res.status_code == 200


def test_create_user():
    res = client.post(
        "/users/", json={"email": "hello123@email.com", "password": "password123"}
    )
    new_user = schemas.UserOut(**res.json())
    new_user.email == "hello123@email.com"
    assert res.status_code == 201
