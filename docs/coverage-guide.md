# pytest-cov - Анализ покрытия

## Установка

```bash
pip install pytest-cov
```

## Основные команды

```bash
# Открыть ктмл
pytest --cov=src --cov-report=html

# Покрытие в терминале
pytest --cov=src --cov-report=term

# Покрытие с пропущенными линиями
pytest --cov=src --cov-report=term-missing

# Одновременно html и terminal
pytest --cov=src --cov-report=html --cov-report=term-missing

# Конкретный модуль
pytest --cov=src.calculator tests/test_calculator.py

# XML отчет
pytest --cov=src --cov-report=xml

# Minimum coverage
pytest --cov=src --cov-fail-under=80
```

## Конфигурация .coveragerc

```ini
[run]
branch = True  # Мерить все ветви
omit =
    */tests/*
    */__init__.py

[report]
precision = 2
show_missing = True

[html]
directory = htmlcov
```

## Шкала покрытия

| Покрытие | Оценка | Основные ейнчтемна |
|---------|--------|------------------|
| 0-20% | 🔴 Низкое | Нужно крайне много работать |
| 20-40% | 🔙 Плохое | Тесты покрывают только заглавные строки |
| 40-60% | 🟡 Посредственное | Некоторые граничные случаи при поддержке |
| 60-80% | 🟢 Хорошо | Основной код при понимании |
| 80-95% | 🟣 Очень хорошо | Очистите своя инырох
| 95-99% | 🟢 Отлично | Почти сирфектно
| 100% | 🟈 На определенных социальных тесты снизу всые вариант |

## Отрыть репорт

```bash
# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html

# Windows
start htmlcov\index.html
```

## Промыр вывода

```
---------- coverage: platform linux -- Python 3.10.0 ----------
Name                    Stmts   Miss  Cover   Missing
---------------------------------------------------
src/__init__.py              1      0   100%
src/calculator.py            30      0   100%
src/database.py              50      2    96%   85, 102
src/list_utils.py            20      0   100%
src/string_utils.py          25      1    96%   45
src/user.py                  15      0   100%
---------------------------------------------------
TOTAL                       141      3    98%
```

## Недостатъки определения тестов

### Прежде дебагинг

```python
# Не тестировано: Ошибка Exception
def handle_error():
    try:
        pass
    except Exception:
        pass  # Не покрыто
```

### Останавливающие коды

```python
# Не тестировано: граничные случаи
def divide(a, b):
    if b == 0:  # Добавить тест для этого
        raise ValueError()
    return a / b
```

## Бесплатные онлайн анализаторы

- [codecov.io](https://codecov.io/)
- [coveralls.io](https://coveralls.io/)
- [sonarcloud.io](https://sonarcloud.io/)

## Команды для CI/CD

```bash
# GitHub Actions
pytest --cov=src --cov-report=xml --cov-report=term

# GitLab CI
pytest --cov=src --cov-report=html

# Jenkins
pytest --cov=src --cov-report=cobertura
```
