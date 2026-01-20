"""
Пример Parametrize
"""
import pytest


def multiply(a, b):
    return a * b


class TestParametrize:
    """Примеры parametrize"""
    
    @pytest.mark.parametrize('a,b,expected', [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 3, -6),
        (1.5, 2, 3),
        (10, 0.1, 1),
    ])
    def test_multiply(self, a, b, expected):
        """Тест основывания с разными аргументами"""
        assert multiply(a, b) == expected
    
    @pytest.mark.parametrize('value', [
        'test1',
        'test2',
        'test3',
    ])
    def test_value_in_list(self, value):
        """Проверить наличие в листе"""
        test_list = ['test1', 'test2', 'test3']
        assert value in test_list


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
