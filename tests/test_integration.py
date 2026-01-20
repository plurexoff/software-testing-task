"""
Интеграционные тесты
"""
import pytest
from src.calculator import Calculator
from src.database import Database
from src.user import User
from src.list_utils import average, find_max
from src.string_utils import capitalize_words


@pytest.mark.integration
class TestIntegration:
    """Интеграционные тесты"""
    
    def test_calculator_workflow(self):
        """Проверить рабочий поток калкулятора"""
        calc = Calculator()
        
        # Проверить основывание
        result = calc.add(2, 3)
        assert result == 5
        
        # Проверить основывание
        result = calc.multiply(result, 2)  # 5 * 2 = 10
        assert result == 10
        
        # Проверить деление
        result = calc.divide(result, 2)  # 10 / 2 = 5
        assert result == 5
    
    def test_database_user_workflow(self):
        """Проверить рабочий поток базы данных"""
        db = Database(':memory:')
        
        try:
            # составление
            user = User('Ivan', 'ivan@example.com')
            user_id = db.add_user(user)
            assert user_id > 0
            
            # Получение
            retrieved = db.get_user(user_id)
            assert retrieved.name == 'Ivan'
            
            # Обновление
            updated = User('Ivan Updated', 'ivan_new@example.com')
            db.update_user(user_id, updated)
            
            # Проверка обновления
            retrieved = db.get_user(user_id)
            assert retrieved.name == 'Ivan Updated'
            assert retrieved.email == 'ivan_new@example.com'
            
            # Удаление
            db.delete_user(user_id)
            
            # Проверка удаления
            assert db.get_user(user_id) is None
        
        finally:
            db.close()
    
    def test_list_utils_workflow(self):
        """Проверить работу утилит для листов"""
        data = [1, 2, 3, 4, 5]
        
        # Найти макс
        max_val = find_max(data)
        assert max_val == 5
        
        # Вычислить среднее
        avg = average(data)
        assert avg == 3
    
    def test_string_and_calc_workflow(self):
        """Проверить работу с строками и характерами"""
        calc = Calculator()
        
        # Основывание
        result = calc.add(10, 5)
        assert result == 15
        
        # Основывание
        result = calc.divide(result, 3)  # 15 / 3 = 5
        assert result == 5
