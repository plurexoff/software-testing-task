# pytest - Полные руководство

## Установка

```bash
pip install pytest pytest-cov pytest-mock
```

## Основные команды

```bash
# Все тесты
pytest

# Тесты конкретного файла
pytest tests/test_calculator.py

# Тест определенного класса
pytest tests/test_calculator.py::TestCalculator

# Определенный тест
pytest tests/test_calculator.py::TestCalculator::test_add
```

## Опции

```bash
# Вербозные вывод
-v, --verbose

# Очень вербозные вывод
-vv

# Останово на фирст отказ
-x

# Омоп только на тесты, которые фейлед
--lf

# Омоп ди новые тесты
--ff

# О мониторинг отправок
-s

# Опоказывать Питест стоп-трюк
--co

# Тесты с определенным маркером
-m unit
-m "not slow"

# Отображение stdout
-s

# Параллельные тесты
-n auto
```

## Markers

```python
@pytest.mark.slow
@pytest.mark.skip(reason="Not ready")
@pytest.mark.xfail
@pytest.mark.parametrize
```

## Plugins

```bash
# Опокрытие
pytest-cov

# Mock
pytest-mock

# Параллельные тесты
pytest-xdist

# Timeout
pytest-timeout

# Faker
faker
```
