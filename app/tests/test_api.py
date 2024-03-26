import pytest
from fastapi.testclient import TestClient

from app.main import app, custom_openapi

client = TestClient(app=app)


def test_api_deposit_1() -> None:
    response = client.post(
        url="/api/v1/deposit/",
        json={"date": "31.01.2021", "periods": 3, "amount": 10000, "rate": 6},
    )
    assert response.status_code == 200
    assert response.json() == {
        "31.01.2021": 10050,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75,
    }


def test_api_deposit_2() -> None:
    response = client.post(
        url="/api/v1/deposit/",
        json={"date": "31.01.2021", "periods": 7, "amount": 10000, "rate": 6},
    )
    assert response.status_code == 200
    assert response.json() == {
        "31.01.2021": 10050,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75,
        "30.04.2021": 10201.51,
        "31.05.2021": 10252.51,
        "30.06.2021": 10303.78,
        "31.07.2021": 10355.29,
    }


def test_api_deposit_invalid_1() -> None:
    response = client.post(
        url="/api/v1/deposit/",
        json={"date": "31-01-2021", "periods": -1, "amount": 9999, "rate": -5},
    )
    assert response.status_code == 400
    assert response.json() == {
        "message": "Input should be greater than 0",
        "type": "greater_than",
    }


def test_api_deposit_invalid_2() -> None:
    response = client.post(
        url="/api/v1/deposit/",
        json={"date": "31", "periods": 5, "amount": 15000, "rate": 1},
    )
    assert response.status_code == 400
    assert response.json() == {
        "message": "Value error, time data '31' does not match format '%d.%m.%Y'",
        "type": "value_error",
    }


def test_api_deposit_invalid_3() -> None:
    response = client.post(
        url="/api/v1/deposit/",
        json={"date": 31, "periods": 5, "amount": 15000, "rate": 1},
    )
    assert response.status_code == 400
    assert response.json() == {
        "message": "Value error, Invalid date, must be 'str' with format '%d.%m.%Y'",
        "type": "value_error",
    }


def test_openapi_scheme() -> None:
    try:
        custom_openapi()
    except Exception as e:
        pytest.fail("Exception raised: " + str(e))
