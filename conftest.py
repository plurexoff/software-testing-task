"""
Выполняемые fixtures pytest
Этот файл автоматически открывается pytest
"""
import pytest
from src.user import User
from src.database import Database


@pytest.fixture
def user_sample():
    """Пример пользователя"""
    return User('Ivan Petrov', 'ivan@example.com')


@pytest.fixture
def users_list():
    """Список пользователей"""
    return [
        User('Ivan', 'ivan@example.com'),
        User('Maria', 'maria@example.com'),
        User('Petr', 'petr@example.com'),
    ]


@pytest.fixture
def db():
    """Новая база данных на каждый тест"""
    return Database(':memory:')  # in-memory database


@pytest.fixture(scope="session")
def test_data():
    """Многоразовые тестовые данные"""
    return {
        'users': [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
            {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'},
        ],
        'numbers': [1, 2, 3, 4, 5],
        'strings': ['hello', 'world', 'test'],
    }
