"""
Тесты модуля list_utils
"""
import pytest
from src.list_utils import (
    find_max, find_min, sum_list, average,
    remove_duplicates, reverse_list
)


class TestListUtils:
    """Тесты утилит для работы с листами"""
    
    # Тесты поиска максимума
    @pytest.mark.parametrize('lst,expected', [
        ([1, 2, 3, 4, 5], 5),
        ([10, 2, 8, 1], 10),
        ([-1, -2, -3], -1),
        ([42], 42),
    ])
    def test_find_max(self, lst, expected):
        assert find_max(lst) == expected
    
    def test_find_max_empty_list(self):
        """Проверить ошибку на пустом листе"""
        with pytest.raises(ValueError):
            find_max([])
    
    # Тесты поиска минимума
    @pytest.mark.parametrize('lst,expected', [
        ([1, 2, 3, 4, 5], 1),
        ([10, 2, 8, 1], 1),
        ([-1, -2, -3], -3),
        ([42], 42),
    ])
    def test_find_min(self, lst, expected):
        assert find_min(lst) == expected
    
    def test_find_min_empty_list(self):
        with pytest.raises(ValueError):
            find_min([])
    
    # Тесты суммы
    @pytest.mark.parametrize('lst,expected', [
        ([1, 2, 3, 4, 5], 15),
        ([0, 0, 0], 0),
        ([-1, 1, 2], 2),
        ([1.5, 2.5], 4),
    ])
    def test_sum_list(self, lst, expected):
        assert sum_list(lst) == expected
    
    # Тесты среднего
    @pytest.mark.parametrize('lst,expected', [
        ([1, 2, 3, 4, 5], 3),
        ([10], 10),
        ([2, 4, 6], 4),
    ])
    def test_average(self, lst, expected):
        assert average(lst) == expected
    
    def test_average_empty_list(self):
        with pytest.raises(ValueError):
            average([])
    
    # Тесты удаления дубликатов
    @pytest.mark.parametrize('lst,expected', [
        ([1, 2, 2, 3, 3, 3], [1, 2, 3]),
        ([1, 1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
    ])
    def test_remove_duplicates(self, lst, expected):
        assert remove_duplicates(lst) == expected
    
    # Тесты отреверсирования
    @pytest.mark.parametrize('lst,expected', [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1], [1]),
        ([], []),
    ])
    def test_reverse_list(self, lst, expected):
        assert reverse_list(lst) == expected
