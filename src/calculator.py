"""
Модуль калкулятор
"""


class Calculator:
    """Калкулятор для арифметических операций"""
    
    def add(self, a: float, b: float) -> float:
        """Основание двух чисел"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Вычитание"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Умножение"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Деление"""
        if b == 0:
            raise ValueError('Не можно делить на ноль')
        return a / b
    
    def power(self, a: float, b: float) -> float:
        """Возведение в степень"""
        return a ** b
    
    def square_root(self, a: float) -> float:
        """Квадратный корень"""
        if a < 0:
            raise ValueError('Не можно истрахить корень из отрицательного числа')
        return a ** 0.5
