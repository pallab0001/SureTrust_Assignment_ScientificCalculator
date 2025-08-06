# Scientific Calculator (No Math Modules)

[![Run on Repl.it](https://replit.com/badge/github/pallab0001/SureTrust_Assignment_ScientificCalculator)](https://replit.com/new/github/YourGitHubUsername/RepoName)

A fully-functional scientific calculator implemented entirely in Python without using any external math libraries. All mathematical operations are custom-built from first principles.

## Features ✨
- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Advanced Functions**:
  - Power and Square Root (Babylonian method)
  - Factorials
  - Trigonometric Functions (Sin, Cos, Tan with Taylor series)
  - Exponential and Natural Logarithm
  - Base Conversion (Binary/Octal/Decimal/Hex)
- **Number Theory**:
  - GCD (Euclidean algorithm)
  - LCM calculation
- **Unit Conversion**:
  - Degrees ⇄ Radians

## Live Demo 🔗
[Try the Calculator Online](https://replit.com/@pallabsardar200/Scientific-Calculator)

## Code Implementation Highlights
```python
# Square root using Babylonian method
def square_root(number):
    if number < 0:
        raise MathError("Square root of negative numbers is not real")
    guess = number / 2
    tolerance = 1e-10
    while True:
        better_guess = (guess + number/guess) / 2
        if abs(better_guess - guess) < tolerance:
            return better_guess
        guess = better_guess

# Sine function using Taylor series
def sine(angle, use_degrees=False, terms=15):
    x = degrees_to_radians(angle) if use_degrees else angle
    result, sign = 0.0, 1
    for n in range(terms):
        exponent = 2 * n + 1
        term = sign * (x ** exponent) / factorial(exponent)
        result += term
        sign *= -1
    return result
