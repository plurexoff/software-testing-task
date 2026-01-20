"""
Пример базовых тестов
"""
import pytest


def simple_add(a, b):
    """Simple function"""
    return a + b


class TestBasic:
    """Базовые тесты"""
    
    def test_simple_add(self):
        """Пример простого теста"""
        assert simple_add(2, 3) == 5
    
    def test_simple_add_with_zero(self):
        """Пример теста с нолем"""
        assert simple_add(5, 0) == 5
    
    def test_simple_add_negative(self):
        """Пример теста с отрицательными числами"""
        assert simple_add(-2, -3) == -5
    
    def test_assertion_error(self):
        """Пример теста с ошибкой"""
        with pytest.raises(AssertionError):
            assert simple_add(2, 3) == 6


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
