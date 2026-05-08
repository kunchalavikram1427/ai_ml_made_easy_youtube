"""
Variables and Typecasting - Explorer Script
============================================
Run: python3 examples.py

This script demonstrates:
- Variable assignment and naming conventions
- All major Python data types
- type(), id(), sys.getsizeof() inspection
- Variable swapping tricks
- Multiple assignment
- Type casting between types
- Mutable vs immutable behavior
"""

import sys

# ============================================================
# SECTION 1: Variable Explorer - Inspecting Python Values
# ============================================================
print("=" * 60)
print("  VARIABLE EXPLORER")
print("=" * 60)

# Let's create different types and inspect them
values = {
    "integer": 42,
    "float": 3.14159,
    "string": "Hello, Python!",
    "boolean": True,
    "none": None,
    "list": [1, 2, 3],
    "tuple": (10, 20, 30),
    "dict": {"key": "value"},
    "complex": 3 + 4j,
}

print(f"\n{'Name':<10} {'Value':<20} {'Type':<25} {'ID':<18} {'Size (bytes)'}")
print("-" * 90)

for name, val in values.items():
    print(f"{name:<10} {str(val):<20} {str(type(val)):<25} {id(val):<18} {sys.getsizeof(val)}")

# ============================================================
# SECTION 2: Integer Caching - Python's Secret Optimization
# ============================================================
print("\n" + "=" * 60)
print("  INTEGER CACHING (Python interns -5 to 256)")
print("=" * 60)

# Small integers are cached — same object in memory
a = 256
b = 256
print(f"\na = {a}, b = {b}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"a is b: {a is b}")  # True — same cached object

# Large integers are NOT cached
x = 1000
y = 1000
print(f"\nx = {x}, y = {y}")
print(f"id(x) = {id(x)}")
print(f"id(y) = {id(y)}")
print(f"x is y: {x is y}")  # May be False — different objects

# ============================================================
# SECTION 3: Dynamic Typing in Action
# ============================================================
print("\n" + "=" * 60)
print("  DYNAMIC TYPING")
print("=" * 60)

x = 42
print(f"\nx = {x}, type = {type(x)}")

x = "now I'm a string"
print(f"x = {x}, type = {type(x)}")

x = [1, 2, 3]
print(f"x = {x}, type = {type(x)}")

x = True
print(f"x = {x}, type = {type(x)}")

# ============================================================
# SECTION 4: Type Casting
# ============================================================
print("\n" + "=" * 60)
print("  TYPE CASTING")
print("=" * 60)

# --- Implicit Type Conversion (Coercion) ---
print("\n--- Implicit Casting (Python does it automatically) ---")
result = 5 + 3.2  # int + float -> float
print(f"5 + 3.2 = {result} (type: {type(result).__name__})")

result2 = True + True + False  # bool in arithmetic: True=1, False=0
print(f"True + True + False = {result2} (type: {type(result2).__name__})")

result3 = 10 * True  # int * bool
print(f"10 * True = {result3} (type: {type(result3).__name__})")

# --- Explicit Type Conversion ---
# int() conversions
print("\n--- int() ---")
print(f"int(3.9) = {int(3.9)}")        # Truncates (not rounds!)
print(f"int(-3.9) = {int(-3.9)}")      # Truncates toward zero
print(f"int('42') = {int('42')}")
print(f"int('FF', 16) = {int('FF', 16)}")  # Hex to int
print(f"int('1010', 2) = {int('1010', 2)}")  # Binary to int
print(f"int(True) = {int(True)}")

# float() conversions
print("\n--- float() ---")
print(f"float(42) = {float(42)}")
print(f"float('3.14') = {float('3.14')}")
print(f"float('inf') = {float('inf')}")

# str() conversions
print("\n--- str() ---")
print(f"str(42) = '{str(42)}'")
print(f"str(3.14) = '{str(3.14)}'")
print(f"str(True) = '{str(True)}'")
print(f"str(None) = '{str(None)}'")
print(f"str([1,2,3]) = '{str([1,2,3])}'")

# bool() conversions — Truthy and Falsy
print("\n--- bool() (Truthy/Falsy) ---")
print("Falsy values:")
falsy_values = [0, 0.0, "", [], {}, (), set(), None, False]
for val in falsy_values:
    print(f"  bool({repr(val):>10}) = {bool(val)}")

print("\nTruthy values:")
truthy_values = [1, -1, 3.14, "hello", [0], {"a": 1}, (0,), True]
for val in truthy_values:
    print(f"  bool({repr(val):>10}) = {bool(val)}")

# Safe casting with error handling
print("\n--- Safe casting ---")
test_values = ["42", "3.14", "hello", "", "True"]
for val in test_values:
    try:
        result = int(val)
        print(f"  int('{val}') = {result}")
    except ValueError:
        print(f"  int('{val}') -> ValueError! Cannot convert.")

# ============================================================
# SECTION 5: Multiple Assignment and Swapping
# ============================================================
print("\n" + "=" * 60)
print("  MULTIPLE ASSIGNMENT & SWAPPING")
print("=" * 60)

# Same value to multiple variables
x = y = z = 0
print(f"\nx = y = z = 0  ->  x={x}, y={y}, z={z}")

# Different values (tuple unpacking)
a, b, c = 10, 20, 30
print(f"a, b, c = 10, 20, 30  ->  a={a}, b={b}, c={c}")

# Pythonic swap (no temp variable!)
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After a, b = b, a: a={a}, b={b}")

# Extended unpacking with *
first, *rest = [1, 2, 3, 4, 5]
print(f"\nfirst, *rest = [1,2,3,4,5]")
print(f"  first = {first}")
print(f"  rest = {rest}")

head, *middle, tail = [1, 2, 3, 4, 5]
print(f"\nhead, *middle, tail = [1,2,3,4,5]")
print(f"  head = {head}")
print(f"  middle = {middle}")
print(f"  tail = {tail}")

# ============================================================
# SECTION 6: Mutable vs Immutable
# ============================================================
print("\n" + "=" * 60)
print("  MUTABLE vs IMMUTABLE")
print("=" * 60)

# Immutable: changing value creates new object
print("\n--- Immutable (int) ---")
x = 10
print(f"x = 10, id(x) = {id(x)}")
x = x + 1
print(f"x = x + 1 -> x = {x}, id(x) = {id(x)}  (NEW object!)")

# Mutable: modifying in place keeps same object
print("\n--- Mutable (list) ---")
my_list = [1, 2, 3]
print(f"my_list = {my_list}, id = {id(my_list)}")
my_list.append(4)
print(f"my_list.append(4) -> {my_list}, id = {id(my_list)}  (SAME object!)")

# Aliasing danger
print("\n--- Aliasing (the trap!) ---")
a = [1, 2, 3]
b = a  # b points to the SAME list
b.append(99)
print(f"a = {a}")  # a is also affected!
print(f"b = {b}")
print(f"a is b: {a is b}")  # True!

# Safe copy
print("\n--- Safe copying ---")
a = [1, 2, 3]
c = a.copy()  # Independent copy
c.append(99)
print(f"a = {a}")  # Unaffected!
print(f"c = {c}")
print(f"a is c: {a is c}")  # False — different objects

# ============================================================
# SECTION 7: Naming Conventions (PEP 8)
# ============================================================
print("\n" + "=" * 60)
print("  NAMING CONVENTIONS (PEP 8)")
print("=" * 60)

# Variables: snake_case
user_name = "Vikram"
total_count = 42

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
PI = 3.14159
DATABASE_URL = "localhost:5432"

print(f"\nVariables (snake_case): user_name = '{user_name}'")
print(f"Constants (UPPER_CASE): MAX_RETRIES = {MAX_RETRIES}")
print(f"Constants (UPPER_CASE): PI = {PI}")
print(f"Constants (UPPER_CASE): DATABASE_URL = '{DATABASE_URL}'")

# ============================================================
# SECTION 8: Variable Scope (Global, Local, LEGB Rule)
# ============================================================
print("\n" + "=" * 60)
print("  VARIABLE SCOPE (LEGB RULE)")
print("=" * 60)

# Local vs Global — shadowing
threshold = 30  # Global variable

def monitor_temperature():
    threshold = 44  # Local — shadows the global
    print(f"  Inside function (local): threshold = {threshold}")

print(f"\nGlobal threshold: {threshold}")
monitor_temperature()
print(f"Global threshold after function call: {threshold}")  # Unchanged!

# Using the 'global' keyword
counter = 0

def increment():
    global counter
    counter += 1

print(f"\ncounter before: {counter}")
increment()
increment()
increment()
print(f"counter after 3 increments: {counter}")  # 3

# Using 'nonlocal' in nested functions
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    print(f"\n  outer() -> inner() call 1: {inner()}")
    print(f"  outer() -> inner() call 2: {inner()}")
    print(f"  outer() -> final count: {count}")

outer()

# LEGB demonstration
x_scope = "global"

def outer_func():
    x_scope_e = "enclosing"

    def inner_func():
        x_scope_l = "local"
        print(f"\n  LEGB Demo:")
        print(f"    Local: x_scope_l = '{x_scope_l}'")
        print(f"    Enclosing: x_scope_e = '{x_scope_e}'")
        print(f"    Global: x_scope = '{x_scope}'")
        print(f"    Built-in: len = {len}")

    inner_func()

outer_func()

# ============================================================
# SECTION 9: del Keyword
# ============================================================
print("\n" + "=" * 60)
print("  del KEYWORD")
print("=" * 60)

# del keyword — removing variable references
print("\n--- Deleting variables ---")
temp_var = 42
print(f"temp_var = {temp_var}")
del temp_var
try:
    print(temp_var)
except NameError as e:
    print(f"After 'del temp_var': {e}")

print("\n" + "=" * 60)
print("  END OF VARIABLES & TYPECASTING DEMO")
print("=" * 60)
