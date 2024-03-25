from fastapi.testclient import TestClient

from app.main import app
from app.tests.other import test_api_deposit_invalid_1_resp_body

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
    assert response.status_code == 422
    assert response.json() == test_api_deposit_invalid_1_resp_body
