# Operators

## Overview

Operators are special symbols (or keywords) that perform operations on values and variables. They are the verbs of programming — they tell Python to *do something* with the data. Every calculation, comparison, and logical decision in your code involves operators.

Python provides a rich set of operators that go beyond basic arithmetic. Understanding operator precedence (which operations happen first) is critical to writing correct expressions. A misplaced operator or a misunderstanding of precedence can lead to subtle bugs that are hard to track down. For example, `2 + 3 * 4` equals `14` (not `20`) because multiplication has higher precedence than addition.

One of Python's strengths is how operators work intuitively with different data types. The `+` operator adds numbers, concatenates strings, and merges lists. The `*` operator multiplies numbers and repeats sequences. This concept is called **operator overloading**, and it makes Python code expressive and readable. By the end of this lesson, you'll be comfortable with all Python operators and know exactly how to control the order of operations.

## Learning Objectives

By the end of this lesson, you will be able to:

- Perform arithmetic operations including floor division and exponentiation
- Compare values using relational operators
- Combine conditions using logical operators (`and`, `or`, `not`)
- Use augmented assignment operators for concise code
- Understand and apply bitwise operators for low-level operations
- Differentiate between `==` (equality) and `is` (identity)
- Test membership with `in` and `not in`
- Apply correct operator precedence in complex expressions
- Use the walrus operator (`:=`) for assignment within expressions
- Build a functional calculator using Python operators

## Prerequisites

- Variables, Data Types & Type Casting (understanding of numeric types, strings)
- Keywords, Syntax & Indentation (understanding of Python syntax and `and`/`or`/`not`/`is`/`in` keywords)

---

## Detailed Explanation

### 1. Arithmetic Operators

These operators perform mathematical calculations:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (true) | `7 / 2` | `3.5` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulo (remainder) | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 10` | `1024` |

```python
# Basic arithmetic
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3 (floor — rounds DOWN to nearest integer)
print(10 % 3)   # 1 (remainder after division)
print(2 ** 10)  # 1024 (2 to the power of 10)

# Division always returns float (even if result is whole number)
print(10 / 2)   # 5.0 (not 5!)
print(type(10 / 2))  # <class 'float'>

# Floor division truncates toward NEGATIVE infinity
print(7 // 2)    # 3
print(-7 // 2)   # -4 (not -3! Rounds toward negative infinity)
print(7 // -2)   # -4

# Modulo — useful for many things
print(15 % 4)    # 3 (remainder)
print(10 % 2)    # 0 (even number check: n % 2 == 0)
print(11 % 2)    # 1 (odd number check: n % 2 != 0)

# Clock arithmetic: What time is it 25 hours from now?
current_hour = 10
hours_later = 25
new_hour = (current_hour + hours_later) % 24  # 11

# Exponentiation
print(2 ** 0)     # 1 (anything to the power 0)
print(2 ** -1)    # 0.5 (negative exponent = reciprocal)
print(9 ** 0.5)   # 3.0 (square root!)
print(27 ** (1/3))  # 3.0 (cube root)

# Large numbers — Python handles arbitrary precision integers
print(2 ** 100)  # 1267650600228229401496703205376
```

#### Operator Overloading with Non-Numeric Types:

```python
# + with strings (concatenation)
greeting = "Hello" + " " + "World"
print(greeting)  # "Hello World"

# * with strings (repetition)
line = "-" * 40
print(line)  # "----------------------------------------"
border = "=-" * 20 + "="
print(border)  # "=-=-=-=-=-=-=-=-=-=-...="

# + with lists (concatenation)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# * with lists (repetition)
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]
```

---

### 2. Comparison/Relational Operators

These operators compare two values and return a boolean (`True` or `False`):

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `5 >= 6` | `False` |

```python
# Numeric comparisons
print(10 == 10)    # True
print(10 == 10.0)  # True (cross-type comparison works for numbers!)
print(10 != 5)     # True
print(5 < 10)      # True
print(10 > 10)     # False
print(10 >= 10)    # True
print(5 <= 4)      # False

# String comparisons (lexicographic — based on Unicode code points)
print("apple" < "banana")   # True ('a' = 97, 'b' = 98)
print("apple" < "Apple")    # False ('a' = 97, 'A' = 65, lowercase > uppercase)
print("abc" == "abc")       # True
print("abc" < "abd")        # True ('c' < 'd')

# Chained comparisons (Python's elegant feature!)
x = 15
print(10 < x < 20)          # True (equivalent to: 10 < x and x < 20)
print(1 <= x <= 100)        # True (is x between 1 and 100?)
print(0 < x < 10)           # False

age = 25
print(18 <= age < 65)       # True (working age)

# Comparison with different types
print(1 == True)    # True (bool is subclass of int)
print(0 == False)   # True
print("1" == 1)     # False (str vs int — no implicit conversion!)
print(None == 0)    # False
print(None == False) # False
print(None == None)  # True (but use 'is None' instead!)
```

---

### 3. Logical Operators

Combine boolean expressions:

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | True if BOTH are True | `True and False` | `False` |
| `or` | True if EITHER is True | `True or False` | `True` |
| `not` | Inverts the boolean | `not True` | `False` |

```python
# Basic logical operations
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

print(not True)         # False
print(not False)        # True

# Real-world example: Access control
is_admin = True
is_active = True
has_permission = False

if is_admin and is_active:
    print("Full access granted")

if is_admin or has_permission:
    print("Can view this page")

if not is_active:
    print("Account is disabled")
```

#### Short-Circuit Evaluation:

Python evaluates logical expressions left to right and stops as soon as the result is determined:

```python
# 'and' short-circuits on False (returns the first falsy value)
print(0 and 42)        # 0 (0 is falsy — stops here, returns 0)
print(42 and 0)        # 0 (42 is truthy — continues, returns 0)
print(42 and "hello")  # "hello" (both truthy — returns last value)
print("" and "hello")  # "" (empty string is falsy — returns "")

# 'or' short-circuits on True (returns the first truthy value)
print(0 or 42)         # 42 (0 is falsy — continues, returns 42)
print(42 or 0)         # 42 (42 is truthy — stops here, returns 42)
print("" or "default") # "default" (common pattern for defaults!)
print(None or "fallback")  # "fallback"

# Practical use of short-circuit for defaults:
username = ""  # Empty (user didn't provide)
display_name = username or "Anonymous"
print(display_name)  # "Anonymous"

# Short-circuit prevents errors:
my_list = []
# This is safe — if list is empty, second condition isn't evaluated
if my_list and my_list[0] > 5:
    print("First element is greater than 5")
# Without short-circuit: my_list[0] would cause IndexError!
```

---

### 4. Assignment Operators

```python
# Basic assignment
x = 10

# Augmented assignment operators (shorthand)
x += 5   # x = x + 5  → 15
x -= 3   # x = x - 3  → 12
x *= 2   # x = x * 2  → 24
x /= 4   # x = x / 4  → 6.0
x //= 2  # x = x // 2 → 3.0
x **= 3  # x = x ** 3 → 27.0
x %= 10  # x = x % 10 → 7.0

# Bitwise augmented assignment
y = 0b1111  # 15
y &= 0b1010  # y = y & 0b1010 → 0b1010 (10)
y |= 0b0101  # y = y | 0b0101 → 0b1111 (15)
y ^= 0b1100  # y = y ^ 0b1100 → 0b0011 (3)
y <<= 2      # y = y << 2 → 0b1100 (12)
y >>= 1      # y = y >> 1 → 0b0110 (6)

# String augmented assignment
message = "Hello"
message += " World"   # "Hello World"
message *= 2          # "Hello WorldHello World"

# List augmented assignment
my_list = [1, 2, 3]
my_list += [4, 5]     # [1, 2, 3, 4, 5] (same as extend)
my_list *= 2          # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
```

---

### 5. Bitwise Operators

These operate on individual bits of integers:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `&` | AND | `5 & 3` | `1` |
| `\|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT (complement) | `~5` | `-6` |
| `<<` | Left shift | `5 << 1` | `10` |
| `>>` | Right shift | `5 >> 1` | `2` |

```python
# Understanding binary representation
a = 5   # Binary: 0101
b = 3   # Binary: 0011

# AND — both bits must be 1
print(f"{a} & {b} = {a & b}")   # 1 (0001)
# 0101
# 0011
# ----
# 0001 → 1

# OR — either bit can be 1
print(f"{a} | {b} = {a | b}")   # 7 (0111)
# 0101
# 0011
# ----
# 0111 → 7

# XOR — bits must differ
print(f"{a} ^ {b} = {a ^ b}")   # 6 (0110)
# 0101
# 0011
# ----
# 0110 → 6

# NOT (bitwise complement): ~n = -(n+1)
print(f"~{a} = {~a}")           # -6

# Left shift — multiply by 2^n
print(f"{a} << 1 = {a << 1}")   # 10 (0101 → 1010)
print(f"{a} << 2 = {a << 2}")   # 20 (0101 → 10100)

# Right shift — divide by 2^n (floor)
print(f"{a} >> 1 = {a >> 1}")   # 2 (0101 → 0010)

# Practical uses of bitwise operators:

# 1. Check if a number is even/odd (faster than modulo)
n = 42
is_even = (n & 1) == 0  # True (last bit is 0 for even numbers)

# 2. Swap without temp variable (XOR swap)
x, y = 10, 20
x ^= y   # x = x ^ y
y ^= x   # y = y ^ (x ^ y) = original x
x ^= y   # x = (x ^ y) ^ x = original y
print(f"x={x}, y={y}")  # x=20, y=10

# 3. Set/clear/toggle specific bits (flags)
READ = 0b100    # 4
WRITE = 0b010   # 2
EXECUTE = 0b001 # 1

permissions = READ | WRITE  # 6 (0b110) — has read and write
print(f"Permissions: {permissions:03b}")  # 110

# Check if has write permission
has_write = bool(permissions & WRITE)  # True

# Add execute permission
permissions |= EXECUTE  # 7 (0b111)

# Remove write permission
permissions &= ~WRITE   # 5 (0b101)

# 4. Powers of 2 with left shift
print(1 << 10)  # 1024 (2^10) — faster than 2**10

# Helper: visualize binary operations
def show_binary_op(a, b, op, symbol):
    result = op(a, b)
    width = max(len(bin(a)), len(bin(b)), len(bin(result))) - 2
    print(f"  {a:>{width}b}  ({a})")
    print(f"{symbol} {b:>{width}b}  ({b})")
    print(f"  {'─' * width}")
    print(f"  {result:>{width}b}  ({result})")
    print()

show_binary_op(12, 10, lambda a, b: a & b, "&")
show_binary_op(12, 10, lambda a, b: a | b, "|")
show_binary_op(12, 10, lambda a, b: a ^ b, "^")
```

---

### 6. Identity Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `is` | Same object in memory | `x is y` |
| `is not` | Different objects in memory | `x is not y` |

```python
# 'is' checks IDENTITY (same object), '==' checks EQUALITY (same value)

# Small integers are cached (-5 to 256)
a = 256
b = 256
print(a == b)   # True (same value)
print(a is b)   # True (same object — cached!)

a = 257
b = 257
print(a == b)   # True (same value)
print(a is b)   # False in many cases (different objects — outside cache)
                # Note: This can be True in some environments due to optimizations

# Lists — mutable objects are never cached
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)   # True (same content)
print(list1 is list2)   # False (different objects!)

list3 = list1
print(list1 is list3)   # True (same object — aliased)

# ALWAYS use 'is' for None comparisons
x = None
print(x is None)      # ✅ Correct and Pythonic
print(x == None)      # Works but not recommended

# Why? Because == can be overridden by a class:
# A class could define __eq__ to return True when compared to None
# 'is' cannot be overridden — it always checks identity

# Useful for checking function return values:
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None

result = find_item([1, 2, 3], 5)
if result is None:
    print("Item not found")
```

---

### 7. Membership Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Value exists in sequence | `3 in [1,2,3]` |
| `not in` | Value does not exist | `4 not in [1,2,3]` |

```python
# Check membership in various sequences

# Lists
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)       # True
print('grape' in fruits)        # False
print('grape' not in fruits)    # True

# Strings (substring check)
message = "Hello, World!"
print('World' in message)       # True
print('world' in message)       # False (case-sensitive!)
print('xyz' not in message)     # True

# Tuples
coordinates = (10, 20, 30)
print(20 in coordinates)        # True

# Dictionaries (checks KEYS, not values!)
user = {'name': 'Vikram', 'age': 28, 'city': 'Hyderabad'}
print('name' in user)           # True (key exists)
print('Vikram' in user)         # False (checking keys, not values!)
print('Vikram' in user.values()) # True (explicitly check values)

# Sets (very fast membership testing — O(1) average)
allowed_extensions = {'.py', '.txt', '.json', '.yaml'}
filename = 'script.py'
extension = '.' + filename.split('.')[-1]
print(extension in allowed_extensions)  # True

# Range (doesn't iterate — O(1) for integers!)
print(50 in range(100))     # True (very fast!)
print(100 in range(100))    # False (range is exclusive of end)

# Practical example: Input validation
valid_choices = {'yes', 'no', 'maybe'}
user_input = input("Enter choice (yes/no/maybe): ").lower()
if user_input in valid_choices:
    print(f"You chose: {user_input}")
else:
    print("Invalid choice!")
```

---

### 8. Operator Precedence and Associativity

From **highest** to **lowest** precedence:

| Precedence | Operator | Description |
|-----------|----------|-------------|
| 1 (highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Multiplication, division, modulo |
| 5 | `+`, `-` | Addition, subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `is not`, `in`, `not in` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 (lowest) | `or` | Logical OR |

```python
# Precedence examples

# ** has higher precedence than unary -
print(-2 ** 2)    # -4 (not 4!) → -(2**2) = -(4) = -4
print((-2) ** 2)  # 4 (explicit parentheses)

# * before +
print(2 + 3 * 4)      # 14 (not 20) → 2 + (3*4) = 2 + 12 = 14
print((2 + 3) * 4)    # 20 (parentheses override)

# Comparison before logical
print(5 > 3 and 2 < 4)  # True → (5>3) and (2<4) = True and True
print(not 5 > 3)         # False → not (5>3) = not True = False
print(not (5 > 3))       # False (same as above — not applies to result)

# Complex expression — use parentheses for clarity!
result = 2 ** 3 ** 2  # Right-to-left associativity for **
# = 2 ** (3 ** 2) = 2 ** 9 = 512 (NOT (2**3)**2 = 64)
print(result)  # 512

# Best practice: USE PARENTHESES when in doubt!
# Even if you know the precedence, parentheses make code clearer
result = (a * b) + (c / d)  # Clear intent
result = a * b + c / d      # Same result, but less obvious

# Associativity — most operators are left-to-right
print(10 - 5 - 2)   # 3 → (10-5)-2 = 5-2 = 3 (left to right)

# ** is right-to-left
print(2 ** 3 ** 2)   # 512 → 2**(3**2) = 2**9 = 512 (right to left)
```

---

### 9. The `round()` Function

```python
# round(number, ndigits) — rounds to specified decimal places
print(round(3.14159))       # 3 (default: round to integer)
print(round(3.14159, 2))    # 3.14
print(round(3.14159, 4))    # 3.1416
print(round(3.5))           # 4
print(round(4.5))           # 4 (!!! Banker's rounding — rounds to EVEN)
print(round(5.5))           # 6

# Banker's Rounding (round half to even):
# When the value is exactly halfway, Python rounds to the nearest EVEN number
# This reduces cumulative rounding errors in financial calculations
print(round(0.5))   # 0 (rounds to even)
print(round(1.5))   # 2 (rounds to even)
print(round(2.5))   # 2 (rounds to even)
print(round(3.5))   # 4 (rounds to even)

# Negative ndigits — round to tens, hundreds, etc.
print(round(1234, -1))   # 1230
print(round(1234, -2))   # 1200
print(round(1234, -3))   # 1000
print(round(1678, -2))   # 1700

# Floating point precision issues
print(0.1 + 0.2)          # 0.30000000000000004 (IEEE 754 limitation)
print(round(0.1 + 0.2, 1))  # 0.3 (round fixes display)

# For financial calculations, use decimal module:
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3 (exact!)
```

---

### 10. The Walrus Operator `:=` (Python 3.8+)

The walrus operator (officially called "assignment expression") assigns a value to a variable as part of an expression:

```python
# Without walrus operator:
line = input("Enter text: ")
while line != "quit":
    print(f"You said: {line}")
    line = input("Enter text: ")

# With walrus operator — eliminates duplication:
while (line := input("Enter text: ")) != "quit":
    print(f"You said: {line}")

# Example: Avoid computing a value twice
import re

text = "Hello, my email is user@example.com"

# Without walrus:
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    email = match.group()
    print(f"Found email: {email}")

# With walrus — more concise:
if (match := re.search(r'\w+@\w+\.\w+', text)):
    print(f"Found email: {match.group()}")

# Example: Filter and transform in list comprehension
numbers = [1, 5, 12, 3, 8, 15, 2, 20]

# Get squares of numbers, but only if the square is > 50
results = [square for n in numbers if (square := n ** 2) > 50]
print(results)  # [144, 64, 225, 400]

# Example: Reading file chunks
# with open('large_file.txt', 'r') as f:
#     while (chunk := f.read(1024)):
#         process(chunk)

# Example: Avoid repeated function calls
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Without walrus — len() called twice:
if len(data) > 5:
    print(f"Long list: {len(data)} items")

# With walrus — len() called once:
if (n := len(data)) > 5:
    print(f"Long list: {n} items")

# IMPORTANT: Don't overuse the walrus operator!
# Use it when it genuinely reduces duplication and improves readability
# Don't use it just to make code shorter — clarity > brevity
```

---

## Code Examples

### Example 1: Complete Operator Demonstration

```python
"""
Comprehensive demonstration of all Python operator types
"""

print("=" * 60)
print(" PYTHON OPERATORS — COMPLETE DEMO")
print("=" * 60)

# --- Arithmetic ---
print("\n🔢 ARITHMETIC OPERATORS")
print(f"  15 + 4  = {15 + 4}")
print(f"  15 - 4  = {15 - 4}")
print(f"  15 * 4  = {15 * 4}")
print(f"  15 / 4  = {15 / 4}")
print(f"  15 // 4 = {15 // 4}")
print(f"  15 % 4  = {15 % 4}")
print(f"  2 ** 10 = {2 ** 10}")

# --- Comparison ---
print("\n🔍 COMPARISON OPERATORS")
a, b = 10, 20
print(f"  a={a}, b={b}")
print(f"  a == b → {a == b}")
print(f"  a != b → {a != b}")
print(f"  a < b  → {a < b}")
print(f"  a > b  → {a > b}")
print(f"  a <= b → {a <= b}")
print(f"  a >= b → {a >= b}")

# --- Logical ---
print("\n🧠 LOGICAL OPERATORS")
x, y = True, False
print(f"  x={x}, y={y}")
print(f"  x and y → {x and y}")
print(f"  x or y  → {x or y}")
print(f"  not x   → {not x}")

# --- Identity ---
print("\n🆔 IDENTITY OPERATORS")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"  list1 == list2  → {list1 == list2}")
print(f"  list1 is list2  → {list1 is list2}")
print(f"  list1 is list3  → {list1 is list3}")

# --- Membership ---
print("\n📋 MEMBERSHIP OPERATORS")
fruits = ['apple', 'banana', 'cherry']
print(f"  'banana' in fruits     → {'banana' in fruits}")
print(f"  'grape' not in fruits  → {'grape' not in fruits}")

# --- Bitwise ---
print("\n💾 BITWISE OPERATORS")
p, q = 12, 10
print(f"  p={p} ({p:04b}), q={q} ({q:04b})")
print(f"  p & q  = {p & q:>2} ({p & q:04b})")
print(f"  p | q  = {p | q:>2} ({p | q:04b})")
print(f"  p ^ q  = {p ^ q:>2} ({p ^ q:04b})")
print(f"  ~p     = {~p:>2}")
print(f"  p << 1 = {p << 1:>2} ({p << 1:04b})")
print(f"  p >> 1 = {p >> 1:>2} ({p >> 1:04b})")
```

### Example 2: Practical Operator Usage

```python
"""
Real-world scenarios where operators are essential
"""

# Scenario 1: Check if a year is a leap year
def is_leap_year(year):
    """A year is a leap year if:
    - Divisible by 4 AND
    - NOT divisible by 100 UNLESS also divisible by 400
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("Leap year check:")
for year in [2000, 1900, 2024, 2023, 2100]:
    print(f"  {year}: {'Yes' if is_leap_year(year) else 'No'}")

# Scenario 2: Simple password validator
def validate_password(password):
    """Check if password meets requirements using operators"""
    has_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    is_valid = has_length and has_upper and has_lower and has_digit
    
    return {
        'valid': is_valid,
        'length_ok': has_length,
        'has_upper': has_upper,
        'has_lower': has_lower,
        'has_digit': has_digit,
    }

print("\nPassword validation:")
result = validate_password("MyPass123")
for check, passed in result.items():
    status = "✓" if passed else "✗"
    print(f"  {status} {check}")

# Scenario 3: FizzBuzz (classic interview problem)
print("\nFizzBuzz (1-20):")
for n in range(1, 21):
    output = ""
    if n % 3 == 0:
        output += "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    print(f"  {n:>2}: {output or n}")

# Scenario 4: Bit flags for permissions (real-world pattern)
class Permission:
    NONE = 0b0000      # 0
    READ = 0b0001      # 1
    WRITE = 0b0010     # 2
    EXECUTE = 0b0100   # 4
    ADMIN = 0b1000     # 8
    ALL = 0b1111       # 15

def check_permission(user_perms, required_perm):
    return bool(user_perms & required_perm)

# User has READ and WRITE
user_perms = Permission.READ | Permission.WRITE  # 3 (0b0011)
print(f"\nPermission check (user has READ|WRITE):")
print(f"  Can read?    {check_permission(user_perms, Permission.READ)}")
print(f"  Can write?   {check_permission(user_perms, Permission.WRITE)}")
print(f"  Can execute? {check_permission(user_perms, Permission.EXECUTE)}")
print(f"  Is admin?    {check_permission(user_perms, Permission.ADMIN)}")
```

### Example 3: Calculator in One Line

```python
"""
The "Calculator in 1 Line" concept
Reference: https://youtube.com/shorts/Xb6wWEcSeuk
"""

# The basic concept — using eval() for a one-line calculator:
# ⚠️ WARNING: eval() is DANGEROUS with untrusted input!
# Never use eval() with user input in production code!

# One-line calculator (educational purposes only):
print(eval(input("Enter expression: ")))

# Safer version with basic validation:
import re

def safe_calc(expression):
    """A safer (but still basic) calculator that only allows math"""
    # Only allow numbers, operators, parentheses, spaces, and decimal points
    if re.match(r'^[\d\s\+\-\*\/\%\.\(\)\*]+$', expression):
        try:
            result = eval(expression)
            return result
        except (SyntaxError, ZeroDivisionError) as e:
            return f"Error: {e}"
    else:
        return "Error: Invalid characters in expression"

# Test expressions
expressions = [
    "2 + 3 * 4",
    "(2 + 3) * 4",
    "2 ** 10",
    "17 % 5",
    "10 / 3",
    "10 // 3",
]

print("Calculator Results:")
print("-" * 40)
for expr in expressions:
    result = safe_calc(expr)
    print(f"  {expr:<20} = {result}")

# Production-safe calculator (without eval):
def calculate(a, b, operator):
    """Safe calculator using operator mapping"""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero",
        '//': lambda x, y: x // y if y != 0 else "Error: Division by zero",
        '%': lambda x, y: x % y if y != 0 else "Error: Division by zero",
        '**': lambda x, y: x ** y,
    }
    
    if operator not in operations:
        return f"Error: Unknown operator '{operator}'"
    
    return operations[operator](a, b)

# Interactive calculator
print("\n\nSafe Calculator:")
print("Supported operators: +, -, *, /, //, %, **")
print("-" * 40)

test_cases = [(10, 3, '+'), (10, 3, '-'), (10, 3, '*'), 
              (10, 3, '/'), (10, 3, '//'), (10, 3, '%'), (2, 10, '**')]

for a, b, op in test_cases:
    result = calculate(a, b, op)
    print(f"  {a} {op} {b} = {result}")
```

### Example 4: Walrus Operator Practical Usage

```python
"""
Practical examples of the walrus operator (:=)
"""

# Example 1: Process data until a condition is met
import random

print("=== Random Walk (stop when |position| > 10) ===")
position = 0
steps = 0
while abs(position := position + random.choice([-1, 1])) <= 10:
    steps += 1
print(f"Walked {steps} steps, ended at position {position}")

# Example 2: Finding items in a list with their properties
data = ["hello", "hi", "extraordinary", "a", "magnificent", "ok"]

# Without walrus — compute len twice or use temp variable
long_words = [(word, len(word)) for word in data if len(word) > 5]

# With walrus — compute len once
long_words = [(word, length) for word in data if (length := len(word)) > 5]
print(f"\nWords longer than 5 chars: {long_words}")

# Example 3: Validating and using input
print("\n=== Input Validation with Walrus ===")
# Simulating with predefined inputs for demo:
test_inputs = ["abc", "-5", "0", "42"]
for test in test_inputs:
    # In real code: while (n := input("Enter a positive number: "))
    if test.lstrip('-').isdigit() and (n := int(test)) > 0:
        print(f"  '{test}' → Valid positive number: {n}")
    else:
        print(f"  '{test}' → Not a valid positive number")
```

---

## Exercises

### Exercise 1: Operator Explorer (Beginner)

**Objective:** Practice all operator types with user input.

**Instructions:**
1. Ask the user to enter two numbers
2. Display the result of ALL arithmetic operations between them
3. Display ALL comparison results between them
4. Show the result of bitwise operations (AND, OR, XOR, shifts)
5. Check if the first number is `in` a range defined by the second number (0 to n)
6. Format output in a clean, readable table

**Expected Output:**
```
Enter first number: 15
Enter second number: 4

╔══ ARITHMETIC ═══════════════════════════╗
║  15 + 4  = 19                           ║
║  15 - 4  = 11                           ║
║  15 * 4  = 60                           ║
║  15 / 4  = 3.75                         ║
║  15 // 4 = 3                            ║
║  15 % 4  = 3                            ║
║  15 ** 4 = 50625                        ║
╠══ COMPARISON ═══════════════════════════╣
║  15 == 4 → False                        ║
║  15 != 4 → True                         ║
║  15 > 4  → True                         ║
║  15 < 4  → False                        ║
╠══ BITWISE ══════════════════════════════╣
║  15 & 4  = 4   (1111 & 0100 = 0100)    ║
║  15 | 4  = 15  (1111 | 0100 = 1111)    ║
║  15 ^ 4  = 11  (1111 ^ 0100 = 1011)    ║
╚═════════════════════════════════════════╝
```

---

### Exercise 2: Expression Evaluator with Precedence (Intermediate)

**Objective:** Build a program that demonstrates and teaches operator precedence.

**Instructions:**
1. Create a list of expressions that demonstrate precedence rules, for example:
   - `2 + 3 * 4` (multiplication before addition)
   - `-2 ** 2` (exponentiation before unary minus)
   - `True or False and False` (and before or)
2. For each expression, show:
   - The expression as written
   - The result Python gives (due to precedence)
   - A parenthesized version showing the actual order of evaluation
   - What a "left-to-right naive" evaluation would give (incorrect)
3. Ask the user to guess the result of 5 random expressions
4. Score them and explain any wrong answers

**Expected Output:**
```
=== Operator Precedence Quiz ===

Question 1: What is the result of  2 + 3 * 4  ?
Your answer: 20
❌ Wrong! The answer is 14
   Explanation: * has higher precedence than +
   Evaluation: 2 + (3 * 4) = 2 + 12 = 14

Question 2: What is the result of  not True or True  ?
Your answer: True
✅ Correct!
   Explanation: 'not' has higher precedence than 'or'
   Evaluation: (not True) or True = False or True = True

Score: 3/5
```

---

### Exercise 3: Full-Featured Calculator — Mini-Project (Advanced)

**Objective:** Build a comprehensive calculator that supports all Python operators.

**Instructions:**
1. Create a calculator with the following features:
   - Basic mode: Two numbers and an operator (safe, no eval)
   - Expression mode: Parse and evaluate mathematical expressions (use eval with sanitization)
   - History: Keep track of last 10 calculations
   - Special functions: `sqrt`, `abs`, `round`, `pow`
   - Conversion mode: Binary ↔ Decimal ↔ Hex ↔ Octal
   - Bitwise mode: Visualize bitwise operations with binary representation
2. Include the "one-line calculator" as a special feature with appropriate warnings about eval()
3. Handle all edge cases: division by zero, invalid input, overflow
4. Add a "explain" command that shows step-by-step evaluation with precedence

**Reference:** The "Calculator in 1 Line" concept from https://youtube.com/shorts/Xb6wWEcSeuk

**Sample Interaction:**
```
=== Python Calculator ===
Modes: [B]asic | [E]xpression | [C]onversion | [Bi]twise | [H]istory | [Q]uit

Mode: b
Enter first number: 10
Operator (+, -, *, /, //, %, **): **
Enter second number: 3
Result: 10 ** 3 = 1000

Mode: e
Expression: (2 + 3) * 4 - 1
Result: 19
Step-by-step:
  1. (2 + 3) = 5    [parentheses first]
  2. 5 * 4 = 20     [multiplication]
  3. 20 - 1 = 19    [subtraction]

Mode: c
Number: 255
Format: decimal
Results:
  Decimal: 255
  Binary:  0b11111111
  Octal:   0o377
  Hex:     0xff

Mode: bi
A: 12 (1100)
B: 10 (1010)
  A & B = 8  (1000)
  A | B = 14 (1110)
  A ^ B = 6  (0110)

Mode: h
Calculation History:
  1. 10 ** 3 = 1000
  2. (2 + 3) * 4 - 1 = 19
  3. 255 → binary: 0b11111111

Mode: q
Goodbye! Total calculations: 3
```

---

## Resources & References

- **Python Official Docs — Expressions:** https://docs.python.org/3/reference/expressions.html
- **Python Official Docs — Operator Precedence:** https://docs.python.org/3/reference/expressions.html#operator-precedence
- **Real Python — Operators and Expressions:** https://realpython.com/python-operators-expressions/
- **Real Python — The Walrus Operator:** https://realpython.com/python-walrus-operator/
- **Programiz — Python Operators:** https://www.programiz.com/python-programming/operators
- **Python Tutor (Visualize expressions):** https://pythontutor.com/
- **PEP 572 — Assignment Expressions (Walrus Operator):** https://peps.python.org/pep-0572/
- **Calculator in 1 Line (YouTube Short):** https://youtube.com/shorts/Xb6wWEcSeuk
- **IEEE 754 Floating Point (why 0.1 + 0.2 ≠ 0.3):** https://floating-point-gui.de/

---

## Key Takeaways

1. **`/` always returns float**, `//` returns floor division (integer if both operands are int)
2. **`%` is modulo** — incredibly useful for cycling, even/odd checks, and clock math
3. **`**` is right-associative** — `2**3**2` = `2**(3**2)` = 512, not 64
4. **`==` checks value, `is` checks identity** — always use `is` for `None`
5. **Short-circuit evaluation** — `and`/`or` don't always evaluate both sides
6. **`and`/`or` return values, not just True/False** — useful for default values
7. **Walrus operator (`:=`)** — assign within expressions; use sparingly for clarity
8. **When in doubt, use parentheses** — they cost nothing and prevent bugs
9. **Bitwise operators** are essential for flags, permissions, and low-level programming
10. **Never use `eval()` with untrusted input** — it can execute arbitrary code

---

