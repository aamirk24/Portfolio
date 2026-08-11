from app import create_app


def test_create_app():
    app = create_app({"TESTING": True})

    assert app.config["TESTING"] is True


def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"I build software that makes complex information useful." in response.data
    assert b"aamirk2405@gmail.com" in response.data
    assert b"https://github.com/aamirk24" in response.data
    assert b"https://www.linkedin.com/in/aamirkhan05/" in response.data
    assert response.data.count(b'class="project-card"') == 6
    assert b"ScholarGraph" in response.data
    assert b"Nonaga" in response.data
    assert b"RepIT" in response.data
    assert b"Auction Website" in response.data
    assert b"Movie Genre Classification" in response.data
    assert b"VibeCheck" in response.data
