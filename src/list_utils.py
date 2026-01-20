"""
Модуль работы с листами
"""
from typing import List, Any


def find_max(lst: List[Any]) -> Any:
    """Найти максимальный элемент"""
    if not lst:
        raise ValueError('Пустой лист')
    return max(lst)


def find_min(lst: List[Any]) -> Any:
    """Найти минимальный элемент"""
    if not lst:
        raise ValueError('Пустой лист')
    return min(lst)


def sum_list(lst: List[float]) -> float:
    """Найти сумму элементов"""
    return sum(lst)


def average(lst: List[float]) -> float:
    """Вычислить среднее значение"""
    if not lst:
        raise ValueError('Пустой лист')
    return sum(lst) / len(lst)


def remove_duplicates(lst: List[Any]) -> List[Any]:
    """Удалить дубликаты"""
    return list(dict.fromkeys(lst))


def reverse_list(lst: List[Any]) -> List[Any]:
    """Отреверсировать лист"""
    return lst[::-1]
