# Unit Test Guide: Arrange, Act, Assert Pattern

Unit testing is a way to check if small parts of your code work correctly. The **Arrange, Act, Assert** pattern is a simple way to organize your tests.

## 1. Arrange
Get everything ready for the test. This means setting up the things you need, like creating objects or preparing data.

```python
# Example in Python
calculator = Calculator()  # Arrange: Make a calculator
number1 = 5
number2 = 3
expected_answer = 8
```

## 2. Act
Do the thing you want to test. This usually means calling a function or running some code.

```python
# Act: Use the calculator to add the numbers
actual_answer = calculator.add(number1, number2)
```

## 3. Assert
Check if the result is what you expected. If it’s not, the test will fail.

```python
# Assert: Make sure the answer is correct
assert actual_answer == expected_answer, f"Expected {expected_answer}, but got {actual_answer}"
```

## Example Test
Here’s a full example using the Arrange, Act, Assert pattern:

```python
def test_addition():
    # Arrange
    calculator = Calculator()
    number1 = 5
    number2 = 3
    expected_answer = 8

    # Act
    actual_answer = calculator.add(number1, number2)

    # Assert
    assert actual_answer == expected_answer, f"Expected {expected_answer}, but got {actual_answer}"
```

## Helpful Tips
- Test one thing at a time to keep it simple.
- Name your tests so it’s clear what they check.
- If your code depends on other parts, you can pretend those parts work perfectly to focus on testing just one thing.

This pattern makes your tests easier to understand and fix if something goes wrong.