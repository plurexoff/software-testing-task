"""
Модуль базы данных
"""
import sqlite3
from typing import List, Optional
from src.user import User


class Database:
    """Подключение к SQLite базе данных"""
    
    def __init__(self, db_path: str = 'users.db'):
        """Инициализация базы"""
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()
    
    def _create_table(self):
        """Составление таблицы"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        self.conn.commit()
    
    def add_user(self, user: User) -> int:
        """Добавить только в базу"""
        self.cursor.execute(
            'INSERT INTO users (name, email) VALUES (?, ?)',
            (user.name, user.email)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Получить пользователя по ID"""
        self.cursor.execute('SELECT id, name, email FROM users WHERE id = ?', (user_id,))
        row = self.cursor.fetchone()
        if row:
            user = User(row[1], row[2])
            user.id = row[0]
            return user
        return None
    
    def get_all_users(self) -> List[User]:
        """Получить всех пользователей"""
        self.cursor.execute('SELECT id, name, email FROM users')
        users = []
        for row in self.cursor.fetchall():
            user = User(row[1], row[2])
            user.id = row[0]
            users.append(user)
        return users
    
    def update_user(self, user_id: int, user: User) -> bool:
        """Обновить на базе"""
        self.cursor.execute(
            'UPDATE users SET name = ?, email = ? WHERE id = ?',
            (user.name, user.email, user_id)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def delete_user(self, user_id: int) -> bool:
        """Удалить из базы"""
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def close(self):
        """Закрыть соединение"""
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
