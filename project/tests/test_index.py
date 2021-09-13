from app.api import index


def test_index(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "welcome!"
    assert response.json()["message"] != "goodbye!"
    assert response.json()["testing"] == True
    assert response.json()["environment"] == "dev"
