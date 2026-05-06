# Comments in Python

## Overview

Comments are one of the most important tools for writing professional, maintainable code. They allow you to explain *why* your code does something (not just *what* it does), leave notes for yourself and other developers, and temporarily disable code during debugging. Python provides several ways to add comments, and knowing when and how to use them is a skill that separates beginners from professionals.

In this lesson, we'll cover every type of comment in Python, establish best practices, and use basic variables to demonstrate comments in real context.

## Learning Objectives

By the end of this lesson, you will be able to:

- Write single-line comments using `#`
- Add inline comments to explain specific lines
- Create multi-line comments using consecutive `#` lines
- Understand docstrings and when they're used (brief intro)
- Apply best practices for writing useful comments
- Know when NOT to comment (avoiding comment noise)

## Prerequisites

- Introduction to Python (understanding what Python is)
- Setting up Environment (Python installed, can run `.py` files)

---

## Detailed Explanation

### 1. Why Comments Matter

Code is read far more often than it is written. Comments help:
- **Future you** — understand code you wrote months ago
- **Team members** — collaborate without guessing intent
- **Debugging** — temporarily disable code to isolate bugs
- **Documentation** — explain complex logic or business rules

```python
# Without comments — what does this do?
x = 86400

# With comments — immediately clear
seconds_per_day = 86400  # 60 sec * 60 min * 24 hours
```

---

### 2. Single-Line Comments (`#`)

The `#` symbol tells Python to ignore everything after it on that line. This is the most common type of comment.

```python
# This is a single-line comment
name = "Vikram"

# You can explain what the next line does
age = 25  # This variable stores the user's age

# Comments can be on their own line
# They can span multiple lines like this
# Each line needs its own # symbol
```

**Rules:**
- Everything after `#` on that line is ignored by Python
- `#` must not be inside a string (otherwise it's just a character)

```python
# This is a comment
message = "# This is NOT a comment — it's part of the string"
print(message)  # Output: # This is NOT a comment — it's part of the string
```

---

### 3. Inline Comments

Inline comments appear on the same line as code, separated by at least two spaces:

```python
x = 10  # Initial counter value
y = x * 2  # Double the counter
temperature = 98.6  # Normal body temperature in Fahrenheit
```

**PEP 8 Guidelines for Inline Comments:**
- Separate them from code by at least **2 spaces**
- Start with `#` followed by **a single space**
- Use sparingly — only when the line needs clarification

```python
# Good — explains WHY, not WHAT
retry_count = 3  # API rate limit allows max 3 retries per minute

# Bad — states the obvious (don't do this)
x = 10  # Set x to 10
```

---

### 4. Multi-Line Comments

Python doesn't have a dedicated multi-line comment syntax (like `/* ... */` in C or Java). Instead, use consecutive single-line comments:

```python
# This function calculates compound interest.
# Formula: A = P(1 + r/n)^(nt)
# Where:
#   P = principal amount
#   r = annual interest rate (decimal)
#   n = number of times compounded per year
#   t = number of years
principal = 1000
rate = 0.05
years = 10
```

---

### 5. Docstrings (Brief Introduction)

Triple-quoted strings (`"""..."""` or `'''...'''`) placed as the first statement in a module, function, class, or method become **docstrings**. They're not technically comments — they're accessible at runtime via `.__doc__` — but they serve a documentation purpose.

```python
"""
This script demonstrates different types of comments in Python.
Author: Vikram
Date: 2024
"""

def greet(name):
    """Display a greeting message for the given name."""
    print(f"Hello, {name}!")

# Access the docstring
print(greet.__doc__)  # Display a greeting message for the given name.
```

> **Note:** We'll cover docstrings in depth in the Functions chapter. For now, just know they exist and serve as documentation for functions, classes, and modules.

---

### 6. Commenting Out Code (Debugging Technique)

During development, you often want to temporarily disable lines of code without deleting them:

```python
name = "Vikram"
age = 25

# Temporarily disabled for debugging:
# print(f"Debug: name={name}, age={age}")

print("Program running normally")

# You can also disable multiple lines:
# old_calculation = x * 2 + y
# result = old_calculation / z
# print(result)

# New approach:
result = (x * 2 + y) / z
print(result)
```

> **Tip:** Most code editors have a shortcut to comment/uncomment selected lines (Cmd+/ on Mac, Ctrl+/ on Windows/Linux).

---

### 7. Best Practices

#### DO:
```python
# Explain WHY, not WHAT
timeout = 30  # Server drops connections after 30s of inactivity

# Explain complex logic
# Use bitwise AND to check if number is even (faster than modulo)
is_even = (number & 1) == 0

# Mark TODOs for future work
# TODO: Add error handling for network timeouts

# Reference related issues or documentation
# See: https://docs.python.org/3/library/functions.html#input
```

#### DON'T:
```python
# Don't state the obvious
x = 5  # assign 5 to x (BAD — adds no value)

# Don't leave outdated comments
# Increment counter by 1
counter = counter + 2  # BAD — comment says 1, code says 2!

# Don't over-comment simple code
# Create a variable called name and set it to Vikram
name = "Vikram"  # BAD — anyone can read this line
```

#### The Golden Rule:
> Write code that's so clear it barely needs comments. Then add comments only where the *intent* isn't obvious from the code itself.

---

## Code Examples

### Example: Comment Types in Action

```python
"""
Module: comment_demo.py
Purpose: Demonstrates all comment types in Python
"""

# ============================================================
# SECTION: Configuration Variables
# ============================================================

# Application settings
app_name = "MyApp"
version = "1.0.0"
debug_mode = True  # Set to False in production

# Database connection parameters
# These values should be loaded from environment variables in production
db_host = "localhost"
db_port = 5432  # PostgreSQL default port

# ============================================================
# SECTION: Basic Calculations
# ============================================================

# Calculate the area of a circle
# Formula: A = pi * r^2
pi = 3.14159
radius = 5
area = pi * radius ** 2  # ** is the exponent operator

# Display results
print(f"Circle with radius {radius}:")
print(f"  Area = {area:.2f}")

# TODO: Add circumference calculation (2 * pi * r)
# TODO: Move these to a geometry module
```

---

## Exercises

### Exercise 1: Comment the Code (Beginner)

Take this uncommented code and add appropriate comments:

```python
x = 100
y = 7
q = x // y
r = x % y
print(f"{x} divided by {y} is {q} remainder {r}")
temp_f = 212
temp_c = (temp_f - 32) * 5 / 9
print(f"{temp_f}F = {temp_c}C")
```

### Exercise 2: Fix the Comments (Intermediate)

These comments are wrong, outdated, or unnecessary. Fix or remove them:

```python
# Set x to 5
x = 10

# Add 1 to the counter
counter = counter - 1

# This prints hello
print("Goodbye!")

name = "Vikram"  # Create a variable called name
```

---

## Resources & References

- **PEP 8 — Comments:** https://peps.python.org/pep-0008/#comments
- **PEP 257 — Docstring Conventions:** https://peps.python.org/pep-0257/
- **Real Python — Writing Comments in Python:** https://realpython.com/python-comments-guide/

---

## Key Takeaways

1. **Use `#` for comments** — everything after it on the line is ignored
2. **Inline comments** need at least 2 spaces before `#`
3. **Multi-line comments** use consecutive `#` lines (no block comment syntax)
4. **Docstrings** (`"""..."""`) document modules, functions, and classes
5. **Comment the WHY, not the WHAT** — code should be self-explanatory
6. **Keep comments updated** — wrong comments are worse than no comments
7. **Use comments to disable code** while debugging (Cmd+/ or Ctrl+/)

---
