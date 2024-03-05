from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_rcr_service():
    commands = ["LEFT", "GRAB", "LEFT", "BACK", "LEFT", "BACK", "LEFT"]
    response = client.post("/commands", json={"commands": commands})
    assert response.status_code == 201

    response = client.get("/rcrs/DROP")
    assert response.status_code == 404

    response = client.get("/rcrs/GRAB")
    assert response.status_code == 200
    assert response.json()["rcr"] == "00"

    response = client.get("/rcrs/BACK")
    assert response.status_code == 200
    assert response.json()["rcr"] == "01"

    response = client.get("/rcrs/LEFT")
    assert response.status_code == 200
    assert response.json()["rcr"] == "1"
