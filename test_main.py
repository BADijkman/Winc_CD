import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_redirect(client):
    response = client.get("/home")
    assert response.status_code == 302
    assert response.location == "/"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Index</title>" in response.data


def test_english_premier_league(client):
    response = client.get("/english_premier_league")
    assert response.status_code == 200
    assert b"<title>English Premier League</title>" in response.data


def test_dutch_eredivisie(client):
    response = client.get("/dutch_eredivisie")
    assert response.status_code == 200
    assert b"<title>Dutch Eredivisie</title>" in response.data

# ******************************************#
# test with error, so site is not deployed when pushed to repositorie


# def test_dutch_eredivisie(client):
#     response = client.get("/dutch eredivisie")
#     assert response.status_code == 200
#     assert b"<title>English Premier League</title>" in response.data
