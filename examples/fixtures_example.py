"""
Пример Fixtures
"""
import pytest


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Database:
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def get_users(self):
        return self.users
    
    def clear(self):
        self.users = []


@pytest.fixture
def user():
    """Фикстура для пользователя"""
    return User('Ivan', 'ivan@example.com')


@pytest.fixture
def db():
    """Фикстура для базы данных"""
    database = Database()
    yield database
    database.clear()  # cleanup


@pytest.fixture
def populated_db(db, user):
    """Фикстура с данными"""
    db.add_user(user)
    return db


class TestFixtures:
    """Примеры fixtures"""
    
    def test_user_fixture(self, user):
        """Простая фикстура"""
        assert user.name == 'Ivan'
        assert user.email == 'ivan@example.com'
    
    def test_db_fixture(self, db, user):
        """Фикстура базы"""
        db.add_user(user)
        users = db.get_users()
        assert len(users) == 1
        assert users[0].name == 'Ivan'
    
    def test_populated_db_fixture(self, populated_db):
        """Фикстура с данными"""
        users = populated_db.get_users()
        assert len(users) == 1
        assert users[0].name == 'Ivan'
    
    def test_fixture_scope(self, user):
        """Эта фикстура создана для каждого теста"""
        assert hasattr(user, 'name')
        assert hasattr(user, 'email')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
