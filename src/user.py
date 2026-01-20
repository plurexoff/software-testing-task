"""
Модель User
"""
from typing import Optional


class User:
    """Класс пользователя"""
    
    def __init__(self, name: str, email: str):
        """Инициализация"""
        if not name or not isinstance(name, str):
            raise ValueError('Название должно быть строкой')
        if not self._validate_email(email):
            raise ValueError('Невалидный е-мейл')
        
        self.name = name
        self.email = email
        self.id: Optional[int] = None
    
    @staticmethod
    def _validate_email(email: str) -> bool:
        """Проверить э-мейл"""
        return '@' in email and '.' in email
    
    def __eq__(self, other) -> bool:
        """Сравнить пользователей"""
        if not isinstance(other, User):
            return False
        return self.name == other.name and self.email == other.email
    
    def __repr__(self) -> str:
        """Строковое представление"""
        return f"User(name='{self.name}', email='{self.email}', id={self.id})"
