"""
Тесты модели User
"""
import pytest
from src.user import User


class TestUser:
    """Тесты класса User"""
    
    def test_user_creation(self):
        """Проверить составление пользователя"""
        user = User('Ivan', 'ivan@example.com')
        assert user.name == 'Ivan'
        assert user.email == 'ivan@example.com'
        assert user.id is None
    
    def test_invalid_name(self):
        """Проверить отказ при пустом названии"""
        with pytest.raises(ValueError):
            User('', 'ivan@example.com')
    
    def test_invalid_email(self):
        """Проверить отказ при невалидном э-мейле"""
        with pytest.raises(ValueError):
            User('Ivan', 'invalid-email')
    
    def test_user_equality(self):
        """Проверить равенство пользователей"""
        user1 = User('Ivan', 'ivan@example.com')
        user2 = User('Ivan', 'ivan@example.com')
        assert user1 == user2
    
    def test_user_inequality(self):
        """Проверить неравенство пользователей"""
        user1 = User('Ivan', 'ivan@example.com')
        user2 = User('Maria', 'maria@example.com')
        assert user1 != user2
    
    def test_user_repr(self):
        """Проверить строковое представление"""
        user = User('Ivan', 'ivan@example.com')
        repr_str = repr(user)
        assert 'Ivan' in repr_str
        assert 'ivan@example.com' in repr_str
