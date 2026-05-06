# Inputs in Python

## Overview

Interactive programs need to communicate with users — and that means accepting input. Python's built-in `input()` function is your primary tool for getting data from users at runtime. While it looks simple on the surface, handling user input properly involves type casting (since `input()` always returns a string), validation (users will enter unexpected things), and patterns for accepting multiple values efficiently.

In this lesson, we'll master the `input()` function, learn common input patterns, build robust input validation, and explore lower-level I/O with `sys.stdin` for more advanced use cases.

## Learning Objectives

By the end of this lesson, you will be able to:

- Use `input()` to accept user data and understand it always returns a string
- Type cast user input to integers, floats, and other types
- Accept multiple values on a single line using `split()` and `map()`
- Build input validation loops with error handling
- Use `sys.stdin` for piped/redirected input
- Create interactive command-line programs

## Prerequisites

- Comments in Python (annotating code)
- Variables and Typecasting (understanding types and casting)
- Advanced Printing (output formatting with f-strings)

---

## Detailed Explanation

### 1. The `input()` Function

The `input()` function pauses program execution, displays an optional prompt, waits for the user to type something and press Enter, then returns what they typed **as a string**.

```python
# Basic string input
name = input("What is your name? ")
print(f"Hello, {name}!")

# IMPORTANT: input() ALWAYS returns a string, even if user types a number
age_str = input("Enter your age: ")
print(type(age_str))  # <class 'str'> — NOT int!
```

#### Key Facts About `input()`:
- **Always returns a string** — even `"42"` is a string, not an integer
- **Strips the trailing newline** — you don't get `\n` at the end
- **Blocks execution** — program waits until user presses Enter
- **Prompt is optional** — `input()` with no argument still works (no prompt shown)

---

### 2. Type Casting User Input

Since `input()` always returns a string, you must explicitly cast to the type you need:

```python
# Integer input
age = int(input("Enter your age: "))
print(f"In 5 years you'll be {age + 5}")

# Float input
height = float(input("Enter your height in meters: "))
print(f"Height: {height:.2f}m")

# One-liner pattern (common in Python)
age = int(input("Enter your age: "))
temperature = float(input("Temperature (C): "))
```

#### What Happens If Casting Fails?

```python
# If user types "hello" instead of a number:
age = int(input("Age: "))  # ValueError: invalid literal for int()

# That's why we need validation (covered below)
```

---

### 3. Multiple Inputs on One Line

Instead of asking multiple questions, you can accept space-separated values:

```python
# Split a single input into parts
x, y = input("Enter two numbers (space-separated): ").split()
# User types: 10 20
# x = "10", y = "20" (still strings!)

# Cast both to integers
x, y = int(x), int(y)
print(f"Sum: {x + y}")

# One-liner using map()
a, b = map(int, input("Enter two integers: ").split())
print(f"{a} + {b} = {a + b}")

# Accept a list of numbers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
```

#### How `map()` Works Here:
```python
# map(function, iterable) applies the function to each item
# input("...").split() returns a list of strings
# map(int, [...]) converts each string to an int

user_input = "10 20 30"
parts = user_input.split()        # ['10', '20', '30']
numbers = list(map(int, parts))   # [10, 20, 30]
```

---

### 4. Input Validation

Users will enter unexpected data. Good programs handle this gracefully:

#### Basic Validation Loop

```python
# Keep asking until valid input is received
while True:
    try:
        age = int(input("Enter your age: "))
        break  # Valid input — exit the loop
    except ValueError:
        print("Please enter a valid number!")

print(f"Your age is {age}")
```

#### Range Validation

```python
while True:
    try:
        age = int(input("Enter your age (1-120): "))
        if 1 <= age <= 120:
            break
        else:
            print("Age must be between 1 and 120!")
    except ValueError:
        print("Please enter a valid number!")
```

#### Yes/No Confirmation

```python
while True:
    answer = input("Continue? (yes/no): ").lower().strip()
    if answer in ("yes", "y"):
        print("Continuing...")
        break
    elif answer in ("no", "n"):
        print("Exiting...")
        break
    else:
        print("Please enter 'yes' or 'no'")
```

#### Menu Selection

```python
menu = """
Choose an option:
  1. Add item
  2. Remove item
  3. View all
  4. Quit
"""

while True:
    print(menu)
    choice = input("Enter choice (1-4): ").strip()
    if choice == "1":
        print("Adding item...")
    elif choice == "2":
        print("Removing item...")
    elif choice == "3":
        print("Viewing all...")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-4.")
```

---

### 5. Common Input Patterns

#### Password Input (Hidden)

```python
import getpass

# Input is hidden (not echoed to terminal)
password = getpass.getpass("Enter password: ")
print(f"Password length: {len(password)}")
```

#### Default Values

```python
name = input("Enter your name [Vikram]: ").strip()
if not name:
    name = "Vikram"  # Use default if user just presses Enter
print(f"Hello, {name}!")

# One-liner with or
name = input("Enter your name [Vikram]: ").strip() or "Vikram"
```

#### Comma-Separated Input

```python
# Accept comma-separated values
tags = input("Enter tags (comma-separated): ").split(",")
tags = [tag.strip() for tag in tags]  # Remove whitespace
print(f"Tags: {tags}")
# User types: python, ai, machine learning
# Output: Tags: ['python', 'ai', 'machine learning']
```

#### Multi-Line Input

```python
# Read lines until user enters a blank line
print("Enter text (blank line to finish):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)
print(f"\nYou entered:\n{text}")
```

---

### 6. `sys.stdin` — Advanced Input

For scripts that receive piped or redirected input (not interactive):

```python
import sys

# Reading from piped input
# Usage: echo "hello world" | python3 script.py
# Or: cat data.txt | python3 script.py

for line in sys.stdin:
    processed = line.strip().upper()
    print(processed)
```

#### `sys.stdout.write()` vs `print()`

```python
import sys

# sys.stdout.write() — no auto-newline, returns character count
sys.stdout.write("Hello\n")      # Must add \n yourself
sys.stdout.write("World\n")

# Equivalent to:
print("Hello")
print("World")
```

#### When to Use `sys.stdin`:
- Processing piped data (`cat file.txt | python3 script.py`)
- Reading from redirected files (`python3 script.py < input.txt`)
- Building Unix-style filter programs
- When you need more control than `input()` provides

---

### 7. Putting It All Together: Interactive Programs

```python
"""
Simple Calculator — demonstrates input patterns
"""

def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")

    while True:
        expression = input("Enter expression (e.g., 5 + 3): ").strip()

        if expression.lower() == "quit":
            print("Goodbye!")
            break

        try:
            parts = expression.split()
            if len(parts) != 3:
                print("Format: number operator number")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print(f"Unknown operator: {operator}")
                continue

            print(f"  = {result}")

        except ValueError:
            print("Error: Invalid numbers. Try again.")

# Uncomment to run:
# calculator()
```

---

## Code Examples

### Example 1: Smart Input Processor

```python
"""
Demonstrates type casting user input with automatic type detection
"""

def smart_cast(value_string):
    """Auto-detect and cast a string to the appropriate type."""
    # Check for None
    if value_string.lower() == "none":
        return None

    # Check for boolean
    if value_string.lower() == "true":
        return True
    if value_string.lower() == "false":
        return False

    # Try int
    try:
        return int(value_string)
    except ValueError:
        pass

    # Try float
    try:
        return float(value_string)
    except ValueError:
        pass

    # Default: return as string
    return value_string


# Test it
test_inputs = ["42", "3.14", "True", "none", "hello", "-7", "0"]
for val in test_inputs:
    result = smart_cast(val)
    print(f"  Input: {val:>8}  ->  Value: {str(result):>8}  Type: {type(result)}")
```

### Example 2: Temperature Converter (Interactive)

```python
"""
Interactive temperature converter with input validation
"""

def get_temperature():
    """Get a valid temperature from user."""
    while True:
        try:
            temp = float(input("Enter temperature value: "))
            return temp
        except ValueError:
            print("Please enter a valid number!")

def get_unit():
    """Get a valid unit choice from user."""
    while True:
        unit = input("Is this (C)elsius or (F)ahrenheit? ").upper().strip()
        if unit in ("C", "F"):
            return unit
        print("Please enter C or F!")

# Uncomment to run interactively:
# temp = get_temperature()
# unit = get_unit()
# if unit == "C":
#     result = (temp * 9/5) + 32
#     print(f"{temp}C = {result:.2f}F")
# else:
#     result = (temp - 32) * 5/9
#     print(f"{temp}F = {result:.2f}C")
```

---

## Exercises

### Exercise 1: Number Guessing Game (Beginner)

**Objective:** Build a number guessing game using `input()` and validation.

**Instructions:**
1. Pick a random number between 1-100 (use `import random; number = random.randint(1, 100)`)
2. Ask the user to guess the number
3. Tell them "Too high!" or "Too low!" after each guess
4. Count the number of attempts
5. Handle invalid input gracefully (non-numbers)
6. Congratulate them when they guess correctly

---

### Exercise 2: Student Grade Calculator (Intermediate)

**Objective:** Accept multiple student scores and calculate statistics.

**Instructions:**
1. Ask how many students
2. For each student, accept their name and score (validate: 0-100)
3. Calculate: average, highest, lowest
4. Print a formatted table of results
5. Use `map()` for bonus: accept all scores on one line

---

### Exercise 3: Interactive To-Do List (Advanced)

**Objective:** Build a command-line to-do app using a menu loop.

**Instructions:**
1. Display a menu: Add, Remove, View, Mark Complete, Quit
2. Use input validation for menu choices
3. Store tasks in a list of dictionaries
4. Handle edge cases (removing from empty list, invalid indices)
5. Format output nicely using f-strings

---

## Resources & References

- **Python Official Docs — input():** https://docs.python.org/3/library/functions.html#input
- **Python Official Docs — sys.stdin:** https://docs.python.org/3/library/sys.html#sys.stdin
- **Real Python — Python Input/Output:** https://realpython.com/python-input-output/
- **Python Official Docs — getpass:** https://docs.python.org/3/library/getpass.html
- **Programiz — Python Input:** https://www.programiz.com/python-programming/input-output-import

---

## Key Takeaways

1. **`input()` always returns a string** — always cast to the type you need
2. **Use `int(input(...))` and `float(input(...))`** for numeric input
3. **`split()` + `map()`** for multiple values on one line
4. **Always validate** — wrap input in `try/except` and check ranges
5. **`while True` + `break`** is the standard input validation pattern
6. **`sys.stdin`** for piped/redirected input in scripts
7. **`.strip()`** removes accidental whitespace from user input
8. **Default values** with `input(...) or "default"` pattern

---
