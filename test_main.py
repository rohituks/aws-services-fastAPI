from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "wikipedia API. call /search or /wiki"}


def test_read_phrase():
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "results": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "44th president",
        ]
    }