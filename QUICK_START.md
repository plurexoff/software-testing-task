# Быстрый старт

## 1️⃣ Установка

```bash
# Клонирование
git clone https://github.com/plurexoff/software-testing-task.git
cd software-testing-task

# Мничение виртуальные окружения (опционально)
python -m venv venv
source venv/bin/activate  # на Windows: venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt
```

## 2️⃣ Запуск тестов

```bash
# Все тесты
pytest

# В вербозном режиме
pytest -v

# Определенные тесты
pytest tests/test_calculator.py -v

# Останов на первом отказе
pytest -x

# Опоказ определенных тестов
pytest -k "test_add"
```

## 3️⃣ Анализ покрытия

```bash
# Покрытие в ктнм
 pytest --cov=src --cov-report=html

# Открыть HTML репорт
open htmlcov/index.html  # на Windows: start htmlcov/index.html

# Покрытие в терминале
pytest --cov=src --cov-report=term-missing
```

## 4️⃣ Примеры

```bash
# Базовые тесты
pytest examples/basic_tests.py -v

# Parametrize
pytest examples/parametrize_example.py -v

# Mocking
pytest examples/mocking_example.py -v

# Fixtures
pytest examples/fixtures_example.py -v
```

## 5️⃣ Основные модули

### Calculator

```python
from src.calculator import Calculator

calc = Calculator()
assert calc.add(2, 3) == 5
assert calc.multiply(4, 5) == 20
assert calc.divide(10, 2) == 5
```

### String Utils

```python
from src.string_utils import reverse_string, is_palindrome, count_vowels

assert reverse_string('hello') == 'olleh'
assert is_palindrome('racecar') == True
assert count_vowels('hello') == 2
```

### List Utils

```python
from src.list_utils import find_max, find_min, average

assert find_max([1, 2, 3, 4, 5]) == 5
assert find_min([1, 2, 3, 4, 5]) == 1
assert average([1, 2, 3]) == 2
```

### User Model

```python
from src.user import User

user = User('Ivan', 'ivan@example.com')
assert user.name == 'Ivan'
assert user.email == 'ivan@example.com'
```

### Database

```python
from src.database import Database
from src.user import User

with Database(':memory:') as db:
    user = User('Ivan', 'ivan@example.com')
    user_id = db.add_user(user)
    retrieved = db.get_user(user_id)
    assert retrieved.name == 'Ivan'
```

## 6️⃣ Маркирование тестов

```bash
# Unit tests only
pytest -m "unit"

# Integration tests only
pytest -m "integration"

# Skip slow tests
pytest -m "not slow"
```

## 7️⃣ Написание новых тестов

```python
# tests/test_my_module.py
import pytest
from src.my_module import my_function

class TestMyModule:
    
    def test_basic(self):
        """Основной тест"""
        assert my_function(2, 3) == 5
    
    @pytest.mark.parametrize('a,b,expected', [
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
    ])
    def test_parametrized(self, a, b, expected):
        """Параметризованные тесты"""
        assert my_function(a, b) == expected
    
    def test_error(self):
        """Проверка ошибок"""
        with pytest.raises(ValueError):
            my_function('invalid', 'args')
```

## 8️⃣ Фикстуры

```python
# tests/test_with_fixtures.py
import pytest
from src.user import User

@pytest.fixture
def sample_user():
    """Create a sample user"""
    return User('Ivan', 'ivan@example.com')

def test_user(sample_user):
    """Test with fixture"""
    assert sample_user.name == 'Ivan'
```

## 📖 Дополнительные ресурсы

- [docs/testing-guide.md](docs/testing-guide.md) - Принципы тестирования
- [docs/pytest-guide.md](docs/pytest-guide.md) - pytest полное руководство
- [docs/coverage-guide.md](docs/coverage-guide.md) - Анализ покрытия
- [ASSIGNMENT.md](ASSIGNMENT.md) - Описание задания
