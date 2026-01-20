"""
Тесты модуля calculator
"""
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Тесты класса Calculator"""
    
    @pytest.fixture
    def calc(self):
        """инстанция калкулятора"""
        return Calculator()
    
    # Тесты основания
    def test_add_positive_numbers(self, calc):
        """Проверить основание положительных чисел"""
        assert calc.add(2, 3) == 5
    
    def test_add_negative_numbers(self, calc):
        """Проверить основание отрицательных чисел"""
        assert calc.add(-2, -3) == -5
    
    def test_add_mixed(self, calc):
        """Проверить основание смешанных чисел"""
        assert calc.add(5, -3) == 2
    
    # Parametrize тесты
    @pytest.mark.parametrize('a,b,expected', [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, -5, 5),
        (1.5, 2.5, 4),
    ])
    def test_add_parametrized(self, calc, a, b, expected):
        """Тест основания с разными аргументами"""
        assert calc.add(a, b) == expected
    
    # Тесты вычитания
    @pytest.mark.parametrize('a,b,expected', [
        (5, 3, 2),
        (0, 0, 0),
        (-1, 1, -2),
    ])
    def test_subtract(self, calc, a, b, expected):
        assert calc.subtract(a, b) == expected
    
    # Тесты умножения
    @pytest.mark.parametrize('a,b,expected', [
        (3, 4, 12),
        (0, 5, 0),
        (-2, 3, -6),
        (1.5, 2, 3),
    ])
    def test_multiply(self, calc, a, b, expected):
        assert calc.multiply(a, b) == expected
    
    # Тесты деления
    @pytest.mark.parametrize('a,b,expected', [
        (10, 2, 5),
        (7, 2, 3.5),
        (-10, 2, -5),
    ])
    def test_divide(self, calc, a, b, expected):
        assert calc.divide(a, b) == expected
    
    def test_divide_by_zero(self, calc):
        """Проверить ошибку при делении на ноль"""
        with pytest.raises(ValueError, match='Не можно делить на ноль'):
            calc.divide(10, 0)
    
    # Тесты возведения в степень
    @pytest.mark.parametrize('a,b,expected', [
        (2, 3, 8),
        (5, 0, 1),
        (2, -1, 0.5),
    ])
    def test_power(self, calc, a, b, expected):
        assert calc.power(a, b) == expected
    
    # Тесты квадратного корня
    @pytest.mark.parametrize('a,expected', [
        (4, 2),
        (9, 3),
        (0, 0),
        (1, 1),
    ])
    def test_square_root(self, calc, a, expected):
        assert calc.square_root(a) == expected
    
    def test_square_root_negative(self, calc):
        """Проверить ошибку при корне из отрицательного"""
        with pytest.raises(ValueError):
            calc.square_root(-1)
