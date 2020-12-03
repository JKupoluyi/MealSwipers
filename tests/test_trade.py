import pytest

from meals.db import get_db


def test_index(client, auth):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Meal Swipers</title>" in response.data


def test_buy(client, auth):
    response = client.get("/")
    assert b"<title>MealSwipers - Buy Page</title>" not in response.data

    auth.login()
    response = client.get("/buy")
    assert b"<td>1</td>" not in response.data
    assert b"<td>2</td>" not in response.data
    assert b"<td>3</td>" in response.data


def test_sell(client, auth):
    auth.login()
    response = client.post("/sell", data={"venmo": "yes", "price": ""})
    assert response.status_code == 200

    response = client.post("/sell", data={"venmo": "", "price": "3"})
    assert response.status_code == 200

    response = client.post("/sell", data={"venmo": "yes", "price": "3"})
    assert response.status_code == 302


def test_view(client, auth):
    auth.login()
    response = client.get("/view/3")
    assert b"Hey test, here" in response.data
    assert b"> 3 </td>" in response.data
    assert b"> other Reviews </h2>" in response.data