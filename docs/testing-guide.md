# Принципы тестирования

## Очновые концепции

### 1. Unit Tests (Очковые тесты)

Тестируют отдельные вновости, методы и внутренне функции.

```python
def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
```

### 2. Integration Tests (Интеграционные тесты)

Тестируют взаимодействие модулей.

```python
@pytest.mark.integration
def test_calculator_workflow():
    calc = Calculator()
    result = calc.add(2, 3)
    result = calc.multiply(result, 2)
    assert result == 10
```

### 3. End-to-End Tests (E2E)

От овержения до результата.

## Типы оссертаций

```python
# Равенство
assert x == y

# Тип данных
assert isinstance(x, int)

# Наличие в коллекции
assert x in y

# Не наличие
assert x not in y

# Нулевуе проверки
assert x is None
assert x is not None

# Тестирование условий
assert x > 0
assert x < 100
assert x >= 0
assert x <= 100

# Оисключения
with pytest.raises(ValueError):
    some_function()
```

## Фикстуры

Принадлежность тестов до их выполнения.

```python
@pytest.fixture
def sample_user():
    return User('Ivan', 'ivan@example.com')

def test_user(sample_user):
    assert sample_user.name == 'Ivan'
```

### Типы scope

- **function** (по умолчанию): Каждый тест
- **class**: Класс тестов
- **module**: Модуль тестов
- **session**: Это до завершения рсех тестов

## Вспомогательные методы

```python
# Setup/Teardown
@pytest.fixture
def resource():
    resource = create_resource()  # Setup
    yield resource
    resource.cleanup()  # Teardown

# Autouse
@pytest.fixture(autouse=True)
def auto_resource():
    # будет автоматически насыщен
    pass

# Parameters
@pytest.fixture(params=['db1', 'db2', 'db3'])
def database(request):
    return Database(request.param)
```

## Покрытие кода

Количество кода, который был исполнен.

### Ideal coverage

- **100%** - Оно не нужно, но во многих ситуациях желательно
- **80%** - Критические части
- **60%** - Минимальные требования

## Best Practices

### 1. Останавливающие случаи

- Пустые листы
- Отрицательные снучайя
- Нулевые значения
- Ошибки

### 2. Наименование

- Название теста должно описывать, что он тестирует
- `test_<function>_<scenario>`

### 3. AAA Pattern

```python
def test_user_creation():
    # Arrange
    expected_name = 'Ivan'
    
    # Act
    user = User('Ivan', 'ivan@example.com')
    
    # Assert
    assert user.name == expected_name
```

### 4. Одна оссертация на тест

```python
# Плохо
def test_user():
    user = User('Ivan', 'ivan@example.com')
    assert user.name == 'Ivan'
    assert user.email == 'ivan@example.com'  # другая ассерт

# Хорошо
def test_user_creation():
    user = User('Ivan', 'ivan@example.com')
    assert user.name == 'Ivan'

def test_user_email():
    user = User('Ivan', 'ivan@example.com')
    assert user.email == 'ivan@example.com'
```
