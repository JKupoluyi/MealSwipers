import pytest

from meals.db import get_db


def test_read(client, auth):
    response = client.get("/")
    assert b"review" not in response.data

    auth.login()
    response = client.get("/review/read/other")
    assert b"test review" in response.data

    response = client.get("/review/read/teqrwr")
    assert b"Reviews for" in response.data

    response = client.get("/review/read/test")
    assert b"Reviews for" in response.data


def test_write(app, client, auth):
    response = client.get("/")
    assert b"review" not in response.data

    auth.login()
    response = client.get("/review/write/1")
    assert b"You are reviewing swipe bought" in response.data

    response = client.get("/review/write/10")
    assert b'Meal swipe not found' == response.data

    response = client.post("/review/write/1", data={"review_star": "1", "review_text": ""})
    assert b'ERROR: Both' in response.data

    response = client.post("/review/write/1", data={"review_star": "1", "review_text": "blah"})
    assert response.status_code == 200

    with app.app_context():
        db = get_db()
        db.execute("UPDATE meal_swipe SET buyer_id = 3 WHERE id = 1")
        db.commit()

    response = client.get("/review/write/1")
    assert b'Only the buyer may write a review' == response.data