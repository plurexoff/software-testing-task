"""
Тесты модуля string_utils
"""
import pytest
from src.string_utils import (
    reverse_string, is_palindrome, count_vowels,
    remove_duplicates, capitalize_words
)


class TestStringUtils:
    """Тесты строковых утилит
    """
    
    @pytest.mark.parametrize('s,expected', [
        ('hello', 'olleh'),
        ('world', 'dlrow'),
        ('', ''),
        ('a', 'a'),
    ])
    def test_reverse_string(self, s, expected):
        assert reverse_string(s) == expected
    
    @pytest.mark.parametrize('s,expected', [
        ('racecar', True),
        ('noon', True),
        ('hello', False),
        ('A man a plan a canal Panama', True),
        ('', True),
    ])
    def test_is_palindrome(self, s, expected):
        assert is_palindrome(s) == expected
    
    @pytest.mark.parametrize('s,expected', [
        ('hello', 2),
        ('aeiou', 5),
        ('bcdfg', 0),
        ('beautiful', 4),
    ])
    def test_count_vowels(self, s, expected):
        assert count_vowels(s) == expected
    
    @pytest.mark.parametrize('s,expected', [
        ('aabbcc', 'abc'),
        ('hello', 'helo'),
        ('aaaa', 'a'),
        ('', ''),
    ])
    def test_remove_duplicates(self, s, expected):
        assert remove_duplicates(s) == expected
    
    @pytest.mark.parametrize('s,expected', [
        ('hello world', 'Hello World'),
        ('python testing', 'Python Testing'),
        ('i am learning', 'I Am Learning'),
    ])
    def test_capitalize_words(self, s, expected):
        assert capitalize_words(s) == expected
