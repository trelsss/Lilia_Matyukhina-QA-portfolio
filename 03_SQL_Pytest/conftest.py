# conftest.py

import psycopg2
import pytest

#настройки подключения к базе данных
DB_SETTINGS = {
    "host": "localhost",       #адрес базы данных
    "port": 5432,              #порт PostgreSQL
    "dbname": "project3",      #имя базы данных
    "user": "postgres",        #имя пользователя
    "password": "Qwert1234"    #пароль
}


@pytest.fixture(scope="session")
def db():
    """
    фикстура создаёт подключение к базе PostgreSQL
    работает один раз за всю сессию тестов
    """
    #подключаемся к базе данных с помощью psycopg2
    conn = psycopg2.connect(**DB_SETTINGS)
    #разрешаем выполнять изменения без вызова commit() вручную
    conn.autocommit = True

    #возвращаем соединение в тесты
    yield conn

    #после завершения всех тестов закрываем подключение
    conn.close()


@pytest.fixture
def cur(db):
    """
    фикстура создаёт курсор для работы с SQL-запросами.
    каждый тест получает "свежий" курсор.
    """
    #создаём курсор из соединения
    c = db.cursor()

    #передаём курсор в тест
    yield c

    #после теста закрываем курсор
    c.close()
