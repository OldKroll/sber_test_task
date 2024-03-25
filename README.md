# Тестовое задание
### Общее
Сборка контейнера:
```shell
$ docker build -t image_name .    
```
Запуск контейнера:
```shell
$ docker run -d -p 3000:8000 image_name   
```
OpenAPI cхема лежит по URL /docs (http://0.0.0.0:3000/docs)
### Описание API
```
POST /api/v1/deposit/
Body: {
  "date": "31.01.2021",
  "periods": 3,
  "amount": 10000,
  "rate": 6
}
---
Response 200:
Body: {
  "31.01.2021": 10050,
  "28.02.2021": 10100.25,
  "31.03.2021": 10150.75
}
---
Response 422:
Body: {
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```



### Тесты

```shell
$  pytest --cov-report term-missing --cov=app app/tests/       

---------- coverage: platform darwin, python 3.12.2-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
app/__init__.py               0      0   100%
app/api/__init__.py           4      0   100%
app/api/v1/__init__.py        4      0   100%
app/api/v1/deposit.py        14      0   100%
app/main.py                   6      0   100%
app/schemes/__init__.py       0      0   100%
app/schemes/deposit.py       12      0   100%
app/tests/__init__.py         0      0   100%
app/tests/other.py            1      0   100%
app/tests/test_api.py        16      0   100%
-------------------------------------------------------
TOTAL                        57      0   100%
     
```
