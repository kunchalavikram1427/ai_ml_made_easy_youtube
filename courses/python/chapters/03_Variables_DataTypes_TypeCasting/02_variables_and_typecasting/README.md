# Variables and Typecasting

## Overview

Variables are one of the most fundamental concepts in programming. In Python, a variable is essentially a name that refers to an object stored in memory. Unlike languages like C or Java, Python uses **dynamic typing**, meaning you don't need to declare the type of a variable before using it — Python figures it out at runtime.

Understanding data types is crucial because every piece of data in Python is an object, and every object has a type. The type determines what operations you can perform on that data, how much memory it occupies, and how Python interprets the underlying bits.

Type casting (also called type conversion) allows you to convert data from one type to another. This is especially important when performing mathematical operations on mixed types or formatting output. Mastering these fundamentals will give you a solid foundation for everything else in Python.

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand how Python variables work as references to objects in memory
- Use `id()`, `type()`, and `sys.getsizeof()` to inspect variables
- Identify and work with all basic Python data types
- Perform explicit and implicit type conversions
- Apply proper variable naming conventions (PEP 8)
- Use multiple assignment and variable swapping techniques
- Differentiate between mutable and immutable types
- Understand variable scope (local, global, LEGB rule) and use `global`/`nonlocal`
- Delete variables with `del` and understand garbage collection basics

## Prerequisites

- Introduction to Python (understanding what Python is, how it works)
- Setting up Environment (Python installed, IDE/editor configured, can run `.py` files)
- Comments in Python (understanding how to annotate code)

## How to Run the Examples

```bash
cd courses/python/chapters/03_Variables_DataTypes_TypeCasting/02_variables_and_typecasting

python3 01_variable_explorer.py            # Inspect types, ids, sizes
python3 02_dynamic_typing.py               # Variables can change type
python3 03_type_casting.py                 # int(), float(), str(), bool()
python3 04_multiple_assignment_swapping.py # Tuple unpacking and swap
python3 05_mutable_vs_immutable.py         # Lists vs tuples, aliasing
python3 06_naming_conventions.py           # PEP 8 and reserved keywords
python3 07_variable_scope.py               # LEGB rule, global, nonlocal
python3 08_keywords.py                     # Lists keywords
```

Each script is self-contained — run them in any order.

---

## Detailed Explanation

### 1. What Are Variables?

In Python, a variable is **not a box that stores data** — it's more like a **label (or sticky note) that points to an object in memory**. When you write `x = 42`, Python creates an integer object `42` somewhere in memory, and the name `x` becomes a reference to that object.

```python
# Creating a variable
x = 42

# The variable 'x' now points to an integer object with value 42
# Think of it as: x --> [42] (object in memory)
```

#### Memory References with `id()`

Every object in Python has a unique identity (memory address). You can inspect it with `id()`:

```python
x = 42
print(id(x))  # e.g., 140234866391344 (memory address)

y = 42
print(id(y))  # Same address! Python reuses small integers (-5 to 256)

z = 1000
w = 1000
print(id(z))  # Different address (outside cached range)
print(id(w))  # May or may not be same (implementation detail)
```

> **Note**: Python caches small integers (-5 to 256) and short strings for performance. This is called **integer interning**.

#### Checking Type with `type()`

```python
x = 42
print(type(x))  # <class 'int'>

name = "Vikram"
print(type(name))  # <class 'str'>

pi = 3.14
print(type(pi))  # <class 'float'>
```

#### Checking Size with `sys.getsizeof()`

```python
import sys

x = 42
print(sys.getsizeof(x))  # 28 bytes (on 64-bit system)

name = "Hello"
print(sys.getsizeof(name))  # 54 bytes

big_num = 10**100
print(sys.getsizeof(big_num))  # Much larger! Python handles arbitrary precision
```

#### Deleting Variables with `del`

You can remove a variable reference using `del`. The object it pointed to will be garbage collected if no other references exist:

```python
x = 42
print(x)  # 42

del x
# print(x)  # NameError: name 'x' is not defined
```

---

### 2. Dynamic Typing in Python

Python is **dynamically typed**, which means:
- You don't declare variable types explicitly
- A variable can change its type during execution
- Type checking happens at runtime, not compile time

```python
# The same variable can hold different types
x = 10          # x is an int
print(type(x))  # <class 'int'>

x = "hello"    # Now x is a string — perfectly valid!
print(type(x))  # <class 'str'>

x = [1, 2, 3]  # Now x is a list
print(type(x))  # <class 'list'>
```

**Contrast with statically typed languages (like Java):**
```java
// Java — you MUST declare the type, and it cannot change
int x = 10;
x = "hello";  // ERROR! Type mismatch
```

**Advantages of dynamic typing:**
- Faster development, less boilerplate
- More flexible code

**Disadvantages:**
- Type errors only caught at runtime
- Can lead to subtle bugs (mitigate with type hints in Python 3.5+)

---

### 3. Python Data Types

#### Numeric Types

```python
# int — whole numbers (arbitrary precision in Python 3)
age = 25
population = 7_900_000_000  # Underscores for readability (Python 3.6+)
hex_val = 0xFF              # Hexadecimal (255)
bin_val = 0b1010            # Binary (10)
oct_val = 0o17              # Octal (15)

# float — decimal numbers (64-bit double precision, IEEE 754)
pi = 3.14159
scientific = 2.5e10         # 25000000000.0
negative_exp = 1.5e-3       # 0.0015
infinity = float('inf')     # Positive infinity
not_a_number = float('nan') # NaN

# complex — numbers with real and imaginary parts
z = 3 + 4j
print(z.real)    # 3.0
print(z.imag)    # 4.0
print(abs(z))    # 5.0 (magnitude)
```

#### String Type

```python
# str — immutable sequence of Unicode characters
name = "Vikram"
greeting = 'Hello, World!'
multiline = """This is a
multi-line string"""

# Raw strings (ignore escape sequences)
path = r"C:\Users\new_folder"  # Backslashes treated literally

# f-strings (formatted string literals, Python 3.6+)
age = 28
message = f"I am {age} years old and will be {age + 1} next year"
```

#### Boolean Type

```python
# bool — True or False (subclass of int)
is_active = True
is_deleted = False

# Booleans are integers under the hood
print(True + True)   # 2
print(True * 10)     # 10
print(False + 1)     # 1

# Truthy and Falsy values
# Falsy: 0, 0.0, '', [], {}, (), set(), None, False
# Truthy: everything else
print(bool(0))       # False
print(bool(42))      # True
print(bool(""))      # False
print(bool("hello")) # True
print(bool([]))      # False
print(bool([1]))     # True
```

#### NoneType

```python
# None — represents the absence of a value (like null in other languages)
result = None
print(type(result))  # <class 'NoneType'>

# Common use cases:
# 1. Default function return
def greet(name):
    print(f"Hello, {name}")

x = greet("World")  # prints "Hello, World"
print(x)            # None (function didn't explicitly return anything)

# 2. Default parameter values
def connect(host, port=None):
    if port is None:
        port = 3306  # default MySQL port
    print(f"Connecting to {host}:{port}")

# 3. Checking for None — always use 'is', not '=='
if result is None:
    print("No result yet")
```

---

### 4. Type Casting (Type Conversion)

#### Implicit Type Conversion (Coercion)

Python automatically converts types in certain situations:

```python
# int + float -> float (int is "promoted" to float)
result = 5 + 3.2
print(result)       # 8.2
print(type(result)) # <class 'float'>

# bool in arithmetic context
total = True + True + False  # 1 + 1 + 0
print(total)  # 2
```

#### Explicit Type Conversion (Casting)

```python
# int() — convert to integer
print(int(3.9))      # 3 (truncates, does NOT round)
print(int("42"))     # 42
print(int("0xFF", 16))  # 255 (specify base)
print(int("1010", 2))   # 10 (binary to int)
print(int(True))     # 1
# print(int("hello"))  # ValueError!

# float() — convert to float
print(float(42))     # 42.0
print(float("3.14")) # 3.14
print(float("inf"))  # inf

# str() — convert to string
print(str(42))       # "42"
print(str(3.14))     # "3.14"
print(str(True))     # "True"
print(str(None))     # "None"
print(str([1,2,3]))  # "[1, 2, 3]"

# bool() — convert to boolean
print(bool(1))       # True
print(bool(0))       # False
print(bool(""))      # False
print(bool(" "))     # True (space is not empty!)
print(bool(None))    # False
print(bool([]))      # False
```

#### Common Type Casting Patterns

```python
# User input is always a string — must cast for math
age_str = "25"
age = int(age_str)
print(f"In 5 years you'll be {age + 5}")

# Safe casting with error handling
user_input = "not_a_number"
try:
    number = int(user_input)
except ValueError:
    print(f"Cannot convert '{user_input}' to integer")
```

---

### 5. Type Checking

```python
# type() — returns the exact type
x = 42
print(type(x) == int)  # True
print(type(x) == float)  # False

# isinstance() — preferred! Considers inheritance
print(isinstance(42, int))         # True
print(isinstance(True, int))       # True (bool is subclass of int)
print(isinstance(42, (int, float)))  # True (check multiple types)

# Why isinstance() is better than type():
# type(True) == int  -> False (exact type is bool)
# isinstance(True, int) -> True (bool inherits from int)
```

---

### 6. Variable Naming Rules and Conventions

#### Rules (will cause SyntaxError if violated):
```python
# Valid variable names
name = "Vikram"
_private = "hidden"
__dunder = "special"
camelCase = "valid but not Pythonic"
name2 = "has numbers"
CONSTANT = 3.14

# Invalid variable names
# 2name = "starts with number"    # SyntaxError
# my-var = "has hyphen"           # SyntaxError
# my var = "has space"            # SyntaxError
# class = "reserved keyword"     # SyntaxError
```

#### PEP 8 Conventions:
```python
# Variables and functions: snake_case
user_name = "Vikram"
total_count = 42

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
PI = 3.14159
DATABASE_URL = "localhost:5432"

# Classes: PascalCase (CamelCase)
# class MyClass:

# Private variables: leading underscore
_internal_value = "private by convention"

# Name mangling: double leading underscore
__mangled = "name mangling in classes"

# Dunder (magic) methods: double underscore both sides
# __init__, __str__, __repr__
```

#### Names to Avoid:
```python
# NEVER use these as variable names — they look like numbers in some fonts:
# l  (lowercase L — looks like 1)
# O  (uppercase O — looks like 0)
# I  (uppercase i — looks like l or 1)

# Avoid overly generic names:
# data, temp, x, thing, stuff, value
# Instead, use descriptive names:
# user_data, temperature, x_coordinate, config_value
```

---

### 7. Multiple Assignment and Swapping

```python
# Multiple assignment (same value)
x = y = z = 0
print(x, y, z)  # 0 0 0

# Multiple assignment (different values) — tuple unpacking
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swapping variables (Pythonic way — no temp variable needed!)
x, y = 10, 20
x, y = y, x  # Swap!
print(x, y)  # 20 10

# How it works under the hood:
# Python creates a tuple (y, x) = (20, 10) on the right side first
# Then unpacks it to x, y on the left side

# Unpacking with * (extended unpacking)
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

head, *middle, tail = [1, 2, 3, 4, 5]
print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5
```

---

### 8. Constants (Convention)

Python doesn't have true constants (unlike `const` in JavaScript or `final` in Java). By convention, we use UPPER_SNAKE_CASE to indicate a value should not be changed:

```python
# Constants — by convention only, Python won't prevent reassignment
PI = 3.14159265358979
MAX_CONNECTIONS = 100
BASE_URL = "https://api.example.com"
DEBUG = False

# AI/Automation relevant constants
MAX_RETRIES = 3
API_TIMEOUT_SECONDS = 30
MODEL_NAME = "claude-3"
BATCH_SIZE = 32
LEARNING_RATE = 0.001

# Python 3.8+ — you can use typing.Final for type checker enforcement
from typing import Final

MAX_SIZE: Final = 100
# MAX_SIZE = 200  # Type checker (mypy) will flag this, but Python won't stop it
```

---

### 9. Mutable vs Immutable (Introduction)

This is a critical concept that affects how variables behave:

```python
# IMMUTABLE types: int, float, str, bool, tuple, frozenset
# Cannot be modified in place — any "change" creates a new object

x = 10
print(id(x))  # e.g., 140234866390992
x = x + 1     # Creates a NEW object, x now points to it
print(id(x))  # Different address!

name = "Hello"
print(id(name))
name = name + " World"  # New string object created
print(id(name))         # Different address!

# MUTABLE types: list, dict, set
# Can be modified in place — same object, same id

my_list = [1, 2, 3]
print(id(my_list))   # e.g., 140234865432128
my_list.append(4)    # Modified in place!
print(id(my_list))   # SAME address!
print(my_list)       # [1, 2, 3, 4]

# Why this matters — aliasing:
a = [1, 2, 3]
b = a              # b points to the SAME object as a
b.append(4)
print(a)           # [1, 2, 3, 4] — a is also affected!
print(a is b)      # True — same object

# To create an independent copy:
c = a.copy()       # or: c = a[:] or c = list(a)
c.append(5)
print(a)           # [1, 2, 3, 4] — a is NOT affected
print(a is c)      # False — different objects
```

---

### 10. Variable Scope — Global and Local

Python resolves variable names using the **LEGB rule** (searched in this order):

| Scope | Description | Example |
|-------|-------------|---------|
| **L**ocal | Inside the current function | Variables defined in a function |
| **E**nclosing | Inside enclosing (outer) functions | Nested function accessing outer function's variable |
| **G**lobal | At the module (file) level | Variables defined at the top level of a `.py` file |
| **B**uilt-in | Python's built-in names | `print`, `len`, `int`, `True` |

#### Local vs Global Scope

```python
threshold = 30  # Global variable

def monitor_temperature():
    threshold = 44  # Local variable — shadows the global!
    print(f"Inside function: {threshold}")  # 44

monitor_temperature()
print(f"Outside function: {threshold}")  # 30 — global is unchanged
```

#### The `global` Keyword

Use `global` to **modify** a global variable from inside a function:

```python
counter = 0  # Global

def increment():
    global counter  # Declares we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2 — global was modified
```

#### The `nonlocal` Keyword

Use `nonlocal` to modify a variable from an enclosing (outer) function:

```python
def outer():
    count = 0  # Enclosing scope variable

    def inner():
        nonlocal count  # Modify the enclosing variable
        count += 1
        print(f"Inner count: {count}")

    inner()  # Inner count: 1
    inner()  # Inner count: 2
    print(f"Outer count: {count}")  # 2

outer()
```

#### LEGB in Action

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(f"inner sees: {x}")  # "local" (L)

    inner()
    print(f"outer sees: {x}")  # "enclosing" (E)

outer()
print(f"module sees: {x}")  # "global" (G)
# print(len)  # <built-in function len> (B)
```

> **Best Practice:** Avoid excessive use of `global`. It makes code harder to test, debug, and reason about. Prefer passing values as function parameters and returning results.

---

## Code Examples

### Example 1: Variable Inspector

```python
"""
Variable Inspector — demonstrates id(), type(), and sys.getsizeof()
"""
import sys

# Create different types of variables
integer_var = 42
float_var = 3.14
string_var = "Python"
bool_var = True
none_var = None
list_var = [1, 2, 3]

# Inspect each variable
variables = {
    'integer_var': integer_var,
    'float_var': float_var,
    'string_var': string_var,
    'bool_var': bool_var,
    'none_var': none_var,
    'list_var': list_var,
}

print(f"{'Name':<15} {'Value':<15} {'Type':<20} {'ID':<20} {'Size (bytes)'}")
print("-" * 85)

for name, value in variables.items():
    print(f"{name:<15} {str(value):<15} {str(type(value)):<20} {id(value):<20} {sys.getsizeof(value)}")
```

### Example 2: Temperature Converter

```python
"""
Temperature Converter — demonstrates type casting and f-strings
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Hardcoded example (input covered in a later video)
temperature = 100.0
unit = "C"

if unit == 'C':
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature}C = {result:.2f}F")
elif unit == 'F':
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature}F = {result:.2f}C")
```

### Example 3: Type Casting Demo

```python
"""
Demonstrates various type casting scenarios and edge cases
"""

print("=== int() conversions ===")
print(f"int(3.7) = {int(3.7)}")          # 3 (truncates toward zero)
print(f"int(-3.7) = {int(-3.7)}")        # -3 (truncates toward zero)
print(f"int('100') = {int('100')}")      # 100
print(f"int('0b1111', 2) = {int('0b1111', 2)}")  # 15
print(f"int(True) = {int(True)}")        # 1
print(f"int(False) = {int(False)}")      # 0

print("\n=== float() conversions ===")
print(f"float(42) = {float(42)}")        # 42.0
print(f"float('3.14') = {float('3.14')}")  # 3.14
print(f"float('inf') = {float('inf')}")    # inf
print(f"float('-inf') = {float('-inf')}")  # -inf

print("\n=== bool() conversions (Truthy/Falsy) ===")
falsy_values = [0, 0.0, '', [], {}, (), set(), None, False]
for val in falsy_values:
    print(f"bool({repr(val):>10}) = {bool(val)}")

print("\n=== Dangerous conversions (will raise errors) ===")
dangerous = [("int('hello')", "ValueError"),
             ("int('')", "ValueError"),
             ("float('abc')", "ValueError")]

for expression, error_type in dangerous:
    try:
        eval(expression)
    except (ValueError, TypeError) as e:
        print(f"{expression:>20} -> {error_type}: {e}")
```

### Example 4: Understanding Mutability

```python
"""
Demonstrates the difference between mutable and immutable objects
"""

print("=== Immutable (int) ===")
a = 10
b = a
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # True — same object (cached small int)
print(f"id(a) = {id(a)}, id(b) = {id(b)}")

a = a + 5  # Creates NEW object
print(f"\nAfter a = a + 5:")
print(f"a = {a}, b = {b}")  # b unchanged!
print(f"a is b: {a is b}")  # False — different objects now

print("\n=== Mutable (list) ===")
list1 = [1, 2, 3]
list2 = list1  # Both point to same object!
print(f"list1 = {list1}, list2 = {list2}")
print(f"list1 is list2: {list1 is list2}")

list1.append(99)  # Modifies in place
print(f"\nAfter list1.append(99):")
print(f"list1 = {list1}, list2 = {list2}")  # BOTH changed!
print(f"list1 is list2: {list1 is list2}")   # Still same object

print("\n=== Safe copying ===")
list3 = list1.copy()  # Independent copy
list3.append(100)
print(f"list1 = {list1}")  # Unaffected
print(f"list3 = {list3}")  # Only list3 has 100
```

---

## Exercises

### Exercise 1: Type Detective (Beginner)

**Objective:** Practice using `type()`, `isinstance()`, and type casting.

**Instructions:**
1. Create variables of each basic type: `int`, `float`, `str`, `bool`, `complex`, `NoneType`
2. Print the type of each variable
3. Convert each to a string and print the result
4. Try converting each to an integer — handle errors gracefully with try/except
5. Create a list of all your variables and loop through them, printing which are numeric types

**Expected Output:**
```
42 is of type <class 'int'>
42 as string: "42"
42 as int: 42

3.14 is of type <class 'float'>
3.14 as string: "3.14"
3.14 as int: 3

... (continue for all types)

Numeric types found: [42, 3.14, (2+3j)]
```

---

### Exercise 2: Smart Input Processor (Intermediate)

**Objective:** Build a function that accepts a string and automatically detects and converts it to the appropriate type.

**Instructions:**
1. Write a function `smart_cast(value_string)` that:
   - Returns `None` if the input is "None" or "none"
   - Returns a `bool` if the input is "True"/"False" (case-insensitive)
   - Returns an `int` if the string represents a whole number
   - Returns a `float` if the string represents a decimal number
   - Returns the original `str` otherwise
2. Test with various inputs: "42", "3.14", "True", "none", "hello", "-7", "0"
3. Print the value and its detected type for each input

**Hint:** Use `try/except` and attempt conversions in order of specificity (most specific first).

---

### Exercise 3: Variable Explorer — Mini-Project (Advanced)

**Objective:** Build a Variable Explorer tool that provides comprehensive information about values.

**Instructions:**
1. Create a script that takes a hardcoded list of values and for each:
   - Displays: value, type, id, memory size (sys.getsizeof)
   - Shows all possible type conversions (which ones succeed/fail)
   - For numbers: show binary, octal, hex representations
   - For strings: show length, is_alpha, is_numeric, is_space
2. Format the output in a nice table or card format

---

## Resources & References

- **Python Official Docs — Built-in Types:** https://docs.python.org/3/library/stdtypes.html
- **Python Official Docs — Built-in Functions (type, id, isinstance):** https://docs.python.org/3/library/functions.html
- **Real Python — Variables in Python:** https://realpython.com/python-variables/
- **Real Python — Basic Data Types:** https://realpython.com/python-data-types/
- **Programiz — Python Variables:** https://www.programiz.com/python-programming/variables-constants-literals
- **Programiz — Type Conversion:** https://www.programiz.com/python-programming/type-conversion-and-casting
- **Python Tutor (Visualize memory references):** https://pythontutor.com/
- **PEP 8 — Naming Conventions:** https://peps.python.org/pep-0008/#naming-conventions

---

## Key Takeaways

1. **Variables are references** — they point to objects in memory, they don't "contain" values
2. **Everything is an object** — even `int`, `bool`, and `None` are objects with `id()` and `type()`
3. **Dynamic typing** — flexible but requires discipline (consider type hints for larger projects)
4. **Type casting** — use `int()`, `float()`, `str()`, `bool()` and collection constructors to convert between types
5. **Mutable vs Immutable** — understanding this prevents countless bugs with shared references
6. **Use `isinstance()` over `type()`** — it respects inheritance and is more Pythonic
7. **Follow PEP 8** — consistent naming makes code readable and professional
8. **Variable scope matters** — understand the LEGB rule; prefer passing parameters over using `global`
9. **`del` frees references** — useful for large objects; garbage collector handles the rest

---
