test_api_deposit_invalid_1_resp_body = {
    "detail": [
        {
            "type": "value_error",
            "loc": ["body", "date"],
            "msg": "Value error, time data '31-01-2021' does not match format '%d.%m.%Y'",
            "input": "31-01-2021",
            "ctx": {"error": {}},
            "url": "https://errors.pydantic.dev/2.6/v/value_error",
        },
        {
            "type": "greater_than",
            "loc": ["body", "periods"],
            "msg": "Input should be greater than 0",
            "input": -1,
            "ctx": {"gt": 0},
            "url": "https://errors.pydantic.dev/2.6/v/greater_than",
        },
        {
            "type": "greater_than",
            "loc": ["body", "amount"],
            "msg": "Input should be greater than 9999",
            "input": 9999,
            "ctx": {"gt": 9999},
            "url": "https://errors.pydantic.dev/2.6/v/greater_than",
        },
        {
            "type": "greater_than",
            "loc": ["body", "rate"],
            "msg": "Input should be greater than 0",
            "input": -5,
            "ctx": {"gt": 0},
            "url": "https://errors.pydantic.dev/2.6/v/greater_than",
        },
    ]
}
