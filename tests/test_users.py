from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app import schemas
from app.config import settings
from app.database import Base, get_db
from app.main import app
from alembic import command


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(engine)

Base.metadata.create_all(bind=engine)


# test dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)


def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "Welcome to fastAPI"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "hello123@email.com", "password": "password123"}
    )
    new_user = schemas.UserOut(**res.json())
    new_user.email == "hello123@email.com"
    assert res.status_code == 201
