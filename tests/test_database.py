"""
Тесты базы данных
"""
import pytest
from src.database import Database
from src.user import User


class TestDatabase:
    """Тесты класса Database"""
    
    @pytest.fixture
    def db(self):
        """Новая база данных для каждого теста"""
        database = Database(':memory:')
        yield database
        database.close()
    
    def test_add_user(self, db):
        """Проверить добавление пользователя"""
        user = User('Ivan', 'ivan@example.com')
        user_id = db.add_user(user)
        assert user_id > 0
    
    def test_get_user(self, db):
        """Проверить получение пользователя"""
        user = User('Ivan', 'ivan@example.com')
        user_id = db.add_user(user)
        
        retrieved_user = db.get_user(user_id)
        assert retrieved_user is not None
        assert retrieved_user.name == 'Ivan'
        assert retrieved_user.email == 'ivan@example.com'
        assert retrieved_user.id == user_id
    
    def test_get_nonexistent_user(self, db):
        """Проверить получение несуществующего пользователя"""
        user = db.get_user(999)
        assert user is None
    
    def test_get_all_users(self, db):
        """Проверить получение всех пользователей"""
        user1 = User('Ivan', 'ivan@example.com')
        user2 = User('Maria', 'maria@example.com')
        
        db.add_user(user1)
        db.add_user(user2)
        
        users = db.get_all_users()
        assert len(users) == 2
        assert users[0].name == 'Ivan'
        assert users[1].name == 'Maria'
    
    def test_update_user(self, db):
        """Проверить обновление пользователя"""
        user = User('Ivan', 'ivan@example.com')
        user_id = db.add_user(user)
        
        updated_user = User('Ivan Updated', 'ivan_new@example.com')
        result = db.update_user(user_id, updated_user)
        
        assert result is True
        retrieved = db.get_user(user_id)
        assert retrieved.name == 'Ivan Updated'
        assert retrieved.email == 'ivan_new@example.com'
    
    def test_delete_user(self, db):
        """Проверить удаление пользователя"""
        user = User('Ivan', 'ivan@example.com')
        user_id = db.add_user(user)
        
        result = db.delete_user(user_id)
        assert result is True
        
        retrieved = db.get_user(user_id)
        assert retrieved is None
    
    def test_context_manager(self):
        """Проверить контекстный менеджер"""
        with Database(':memory:') as db:
            user = User('Ivan', 'ivan@example.com')
            user_id = db.add_user(user)
            assert db.get_user(user_id) is not None
