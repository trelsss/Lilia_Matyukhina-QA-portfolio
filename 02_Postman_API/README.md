# Project 2 — API-тестирование (Postman)

Что внутри
- \collection.json\ — коллекция запросов Postman (v2.1)
- \environment.json\ — переменные окружения (baseUrl, токены и пр.)
- \docs/\ — отчёты/скриншоты запусков (по желанию)

Как открыть
1. Postman → **Import** → выберите \collection.json\ и \environment.json\
2. Выберите Environment и запустите коллекцию.

Проверки (примеры)
- Статусы (200/201/400/401)
- Content-Type: application/json
- Структура ответа (ключевые поля)
- Авторизация/токены
- Пагинация и фильтры

Автотесты в Postman
Скрипты в разделе **Tests** (pm.test / chai assertions).

