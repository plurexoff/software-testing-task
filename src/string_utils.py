"""
Модуль работы со строками
"""


def reverse_string(s: str) -> str:
    """Отреверсировать строку"""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Проверить, является ли строка палиндомомом"""
    clean_s = s.lower().replace(' ', '')
    return clean_s == clean_s[::-1]


def count_vowels(s: str) -> int:
    """Осбитать гласные в строке"""
    vowels = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return sum(1 for char in s if char in vowels)


def remove_duplicates(s: str) -> str:
    """Удалить дубликаты в строке"""
    seen = set()
    return ''.join(c for c in s if not (c in seen or seen.add(c)))


def capitalize_words(s: str) -> str:
    """Нанисать каждое слово заглавнымим"""
    return ' '.join(word.capitalize() for word in s.split())
