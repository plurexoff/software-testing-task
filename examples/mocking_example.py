"""
Пример Mocking
"""
import pytest
from unittest.mock import Mock, patch, MagicMock


class DataService:
    def get_data(self):
        # На самом деле функция наружу
        pass


class TestMocking:
    """Примеры mocking"""
    
    def test_mock_simple(self):
        """Простое мокирование"""
        # Сшюють объект
        mock_obj = Mock()
        mock_obj.method.return_value = 'mocked_value'
        
        # Проверить
        assert mock_obj.method() == 'mocked_value'
        mock_obj.method.assert_called_once()
    
    def test_mock_with_side_effect(self):
        """Мокирование с side effect"""
        mock_func = Mock(side_effect=[10, 20, 30])
        
        assert mock_func() == 10
        assert mock_func() == 20
        assert mock_func() == 30
    
    def test_mock_with_exception(self):
        """Мокирование с оисключением"""
        mock_obj = Mock()
        mock_obj.method.side_effect = ValueError('Ошибка!')
        
        with pytest.raises(ValueError):
            mock_obj.method()
    
    def test_patch_with_context_manager(self):
        """Патч с контекстным менеджером"""
        with patch.object(DataService, 'get_data') as mock_method:
            mock_method.return_value = [1, 2, 3]
            
            service = DataService()
            result = service.get_data()
            
            assert result == [1, 2, 3]
            mock_method.assert_called_once()
    
    def test_mock_call_count(self):
        """Проверить количество вызовов"""
        mock_func = Mock(return_value=42)
        
        mock_func()
        mock_func()
        mock_func()
        
        assert mock_func.call_count == 3
    
    def test_mock_call_args(self):
        """Проверить аргументы вызова"""
        mock_func = Mock()
        
        mock_func('arg1', 'arg2', key='value')
        
        mock_func.assert_called_with('arg1', 'arg2', key='value')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
