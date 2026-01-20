# Задание №5: Тестирование ПО

Репозиторий для практического задания по написанию тестов для Python кода и анализу покрытия.

## 📋 Цель задания

Научиться:
- Написанию юнит-тестов
- Написанию интеграционных тестов
- Организации тестов
- Анализу покрытия кода
- Мокингу и fixtures

## 📁 Структура проекта

```
software-testing-task/
├── README.md
├── ASSIGNMENT.md              # Описание задания
├── requirements.txt            # Зависимости
├── pytest.ini                 # Конфигурация pytest
├── conftest.py               # Поделяемые fixtures
├── setup.py                  # Упаковка проекта
├── .coveragerc              # Конфиг для pytest-cov
├── .gitignore
├── src/                      # Основной код
│   ├── __init__.py
│   ├── calculator.py           # Модуль калкулятор
│   ├── string_utils.py         # Модуль работы со строками
│   ├── list_utils.py           # Модуль работы с листами
│   ├── user.py                 # Класс User
│   └── database.py             # Модуль базы данных
├── tests/                    # Тесты
│   ├── __init__.py
│   ├── test_calculator.py      # Тесты калкулятора
│   ├── test_string_utils.py    # Тесты работы со строками
│   ├── test_list_utils.py      # Тесты листов
│   ├── test_user.py            # Тесты User
│   ├── test_database.py        # Интеграционные тесты
│   ├── test_integration.py     # Интеграционные тесты
│   └── fixtures.py             # Вспомогательные fixtures
├── examples/                 # Примеры
│   ├── basic_tests.py          # Базовые тесты
│   ├── parametrize_example.py  # Parametrize
│   ├── mocking_example.py      # Mocking
│   └── fixtures_example.py     # Fixtures
├── docs/                     # Документация
│   ├── testing-guide.md        # Принципы тестирования
│   ├── pytest-guide.md         # Принципы pytest
│   └── coverage-guide.md       # pytest-cov
└── .github/workflows/        # CI/CD
    └── tests.yml              # GitHub Actions
```

## ⚠️ Предпосылки

- Python 3.8+
- pytest
- pytest-cov
- pytest-mock

## 🚀 Как использовать

### 1. Клонирование репозитория

```bash
git clone https://github.com/plurexoff/software-testing-task.git
cd software-testing-task
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Запуск тестов

```bash
# Все тесты
pytest

# Тесты конкретного модуля
pytest tests/test_calculator.py

# Читаемые результаты
pytest tests/test_calculator.py -v

# Нестопор при первом отказе
pytest -x

# Прокажу тесты, которые отказали
pytest --lf

# Покрытие кода
pytest --cov=src --cov-report=html --cov-report=term

# Покрытие конкретного модуля
pytest --cov=src/calculator tests/test_calculator.py

# Маркированные тесты
pytest -m "not slow"
```

### 4. Примеры

```bash
# Базовые тесты
python examples/basic_tests.py

# Parametrize
pytest examples/parametrize_example.py -v

# Mocking
pytest examples/mocking_example.py -v

# Fixtures
pytest examples/fixtures_example.py -v
```

## 📚 Основные концепции

### Типы тестов

- **Unit Tests** - тестирование отдельных функций
- **Integration Tests** - тестирование взаимодействия модулей
- **End-to-End Tests** - тестирование целых сценариев

### Assert Операторы

```python
assert x == y              # Проверка равенства
assert x is not None       # Проверка наличия
assert len(x) > 0          # Проверка длины
assert isinstance(x, int)  # Проверка типа
assert x in y              # Проверка наличия в коллекции
```

### Fixtures

```python
@pytest.fixture
def user():
    return User('Ivan', 'ivan@example.com')

def test_user(user):
    assert user.name == 'Ivan'
```

### Parametrize

```python
@pytest.mark.parametrize('a,b,expected', [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### Mocking

```python
from unittest.mock import Mock, patch

def test_with_mock(mocker):
    mock_db = mocker.patch('src.database.Database')
    mock_db.get_user.return_value = {'name': 'Ivan'}
    result = get_user(1)
    assert result['name'] == 'Ivan'
```

## 🧪 Покрытие кода

```bash
# Покрытие всего проекта
pytest --cov=src --cov-report=html

# Открыть htmlcov/index.html в браузере
```

## 🤏 Новичку: откуда начинать

1. Читать `docs/testing-guide.md`
2. Мотреть `examples/basic_tests.py`
3. Рану тесты: `pytest tests/test_calculator.py -v`
4. Написать свои тесты
5. Проверить покрытие: `pytest --cov=src`

## 📖 Дополнительные ресурсы

- [pytest официальная документация](https://docs.pytest.org/)
- [pytest-cov](https://pytest-cov.readthedocs.io/)
- [Принципы тестирования](https://docs.pytest.org/en/stable/example/index.html)
- [Mock objects](https://docs.python.org/3/library/unittest.mock.html)

## 👤 Автор

plurexoff

## 📄 Лицензия

MIT
