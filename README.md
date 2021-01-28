# Qmobi_test_http_Api
Сервис конверта валют (USD->RUB; USD->EUR и т.д.) <br/>
Запуск - ```python start_server.py``` <br/>
Пример запроса - ```requests.get('http://127.0.0.1:8000/usd-rub?value=1131')``` <br/>
Ответ - ```{"start_currency": "usd", "final_currency": "rub", "start_value": "1131", "final_value": 86259.6735}``` <br/>
Для запуска в котейнере создан и настроен Dockerfile
