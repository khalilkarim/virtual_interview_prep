import pytest
import database
from app import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", tmp_path / "test.db")
    database.init_db()
    app.config["TESTING"] = True
    return app.test_client()


def test_get_answers(client):
    res = client.get("/api/answers")
    assert res.get_json() == []
    assert res.status_code == 200


def test_add_answers(client):
    res = client.post(
        "/api/answers", json={"question_id": 1, "text": "I am a software Engineer"}
    )
    assert res.status_code == 201
    assert res.get_json()["question_id"] == 1
    assert res.get_json()["text"] == "I am a software Engineer"

def test_add_answer_inserts_into_db(client):
    post = client.post("/api/answers", json={"question_id": 1, "text": "I am a software Engineer"})
    res = client.get("/api/answers")
    assert post.status_code == 201
    assert res.get_json() == [{"id": 1, "question_id": 1, "text": "I am a software Engineer"}]


def test_add_users_without_answer_id_returns_400(client):
    res = client.post("/api/answers", json={"text": "I am a software Engineer"})
    assert res.status_code == 400


def test_add_answers_without_text_returns_400(client):
    res = client.post("/api/answers", json={"question_id": 1})
    assert res.status_code == 400

def test_add_answer_with_unknown_question_id_returns_400(client):
    res = client.post("/api/answers", json={"question_id": 99, "text": "I am a software Engineer"})
    assert res.status_code == 400

def test_add_answer_with_empty_text_returns_400(client):
    res = client.post("/api/answers", json={"question_id": 1, "text": "    "})
    assert res.status_code == 400
