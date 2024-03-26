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
Response 400:
Body: {
  "detail": [
    {
      "message": "string",
      "type": "string"
    }
  ]
}

```



### Тесты

```shell
$  pytest --cov-report term-missing --cov=app app/tests/       

---------- coverage: platform darwin, python 3.12.2-final-0 ----------
Name                                      Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------
app/__init__.py                               0      0   100%
app/api/__init__.py                           4      0   100%
app/api/v1/__init__.py                        4      0   100%
app/api/v1/deposit.py                        14      0   100%
app/main.py                                  22      3    86%   28, 35-36
app/schemes/__init__.py                       0      0   100%
app/schemes/deposit.py                       14      1    93%   17
app/tests/__init__.py                         0      0   100%
app/tests/other.py                            1      1     0%   1
app/tests/test_api.py                        25      2    92%   64-65
app/utils/__init__.py                         0      0   100%
app/utils/validation/__init__.py              0      0   100%
app/utils/validation/custom_handlers.py       9      0   100%
app/utils/validation/error.py                 7      0   100%
-----------------------------------------------------------------------
TOTAL                                       100      7    93%

     
```
