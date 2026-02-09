# Installing and Using pytest-cov

### What is pytest-cov?
pytest-cov is a tool that shows you which parts of your code are covered by tests. It generates a **coverage report** that tells you:
- Which lines of code were run during testing
- Which lines were never executed by your tests
- The percentage of your code that is tested

This helps you identify parts of your code that need more tests.

### How to Install pytest-cov

**Step 1:** Make sure your virtual environment is activated. If you see `(venv)` at the beginning of your terminal prompt, it's activated. If not, run:
```bash
source venv/bin/activate
```

**Step 2:** Install pytest-cov using pip:
```bash
pip install pytest-cov
```

### How to Run Tests with Coverage

**Step 1:** Click on the 'Testing' icon in the left navigation bar (hint: it looks like a beaker).

**Step 2:** Click the 'Run Test with Coverage' option next to the test(s) you want to run.

**Step 3:** View the 'Test Coverage' section in the Test Explorer panel to see the coverage report for each file.

# Unit Test Guide: ARRANGE, ACT, ASSERT Pattern

Unit testing is a way to check if small parts of your code work correctly. The **ARRANGE, ACT, ASSERT** pattern is a simple way to organize your tests.

## 1. ARRANGE
Get everything ready for the test. This means setting up the things you need, like creating objects or preparing data.

```python
# Example in Python
calculator = Calculator()  # ARRANGE: Make a calculator
number1 = 5
number2 = 3
expected_answer = 8
```

## 2. ACT
Do the thing you want to test. This usually means calling a function or running some code.

```python
# ACT: Use the calculator to add the numbers
actual_answer = calculator.add(number1, number2)
```

## 3. ASSERT
Check if the result is what you expected. If it’s not, the test will fail.

```python
# ASSERT: Make sure the answer is correct
assert actual_answer == expected_answer, f"Expected {expected_answer}, but got {actual_answer}"
```

## Example Test
Here’s a full example using the ARRANGE, AC, ASSERT pattern:

```python
def test_addition():
    # ARRANGE
    calculator = Calculator()
    number1 = 5
    number2 = 3
    expected_answer = 8

    # ACT
    actual_answer = calculator.add(number1, number2)

    # ASSERT
    assert actual_answer == expected_answer, f"Expected {expected_answer}, but got {actual_answer}"
```

## Helpful Tips
- Test one thing at a time to keep it simple.
- Name your tests so it’s clear what they check.
- If your code depends on other parts, you can pretend those parts work perfectly to focus on testing just one thing.

This pattern makes your tests easier to understand and fix if something goes wrong.