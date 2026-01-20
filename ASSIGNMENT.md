# Задание №5: Тестирование ПО

## Описание

Освоить написание юнит-тестов, интеграционных тестов и анализа покрытия кода.

## Требования

### 1. Подключение pytest

```bash
# Установка
pip install pytest pytest-cov pytest-mock

# Запуск
 pytest
```

### 2. Написание тестов

Тесты должны тестировать:

- Правильность основного функционала
- Граничные случаи
- Останавливающие састояния
- Ошибки и исключения

### 3. Категоризация тестов

```python
# Маркирование
@pytest.mark.unit      # Очковые тесты
@pytest.mark.integration  # Интеграционные тесты
@pytest.mark.slow      # Медленные тесты
@pytest.mark.smoke     # Останавливающие тесты
```

### 4. Fixtures

```python
@pytest.fixture
def resource():
    # Setup
    yield resource_object
    # Teardown
```

### 5. Parametrize

```python
@pytest.mark.parametrize('a,b,expected', [
    (2, 3, 5),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## Команды pytest

```bash
# Все тесты
pytest

# Тесты конкретного модуля
pytest tests/test_calculator.py

# Маркированные тесты
pytest -m unit
pytest -m "not slow"

# Покрытие
pytest --cov=src --cov-report=html --cov-report=term

# Вербозные результаты
pytest -v

# Остановить на первом файле
pytest -x

# Показать неудачные тесты
pytest --lf

# Покажите тесты не на диске
pytest --co
```

## Анализ покрытия

```bash
# Покрытие в HTML жанре
pytest --cov=src --cov-report=html
open htmlcov/index.html

# Покрытие работая
 pytest --cov=src --cov-report=term-missing
```

## Мокинг

```python
from unittest.mock import Mock, patch, MagicMock

# Мок
 mock_obj = Mock()
mock_obj.method.return_value = 'value'

# Patch
with patch('module.Class') as mock_class:
    mock_class.return_value = Mock(method=Mock(return_value=42))

# Мокирование с pytest-mock
def test_func(mocker):
    mock = mocker.patch('module.function')
    mock.return_value = 'mocked'
```
