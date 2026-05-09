"""
Variable Explorer — Inspecting Python Values
==============================================
Run: python3 01_variable_explorer.py

Demonstrates:
- Creating different Python data types
- Using type() to check types
- Using id() to see memory addresses
- Using sys.getsizeof() to check memory usage
"""

import sys

# =============================================================================
# INSPECTING PYTHON VALUES
# =============================================================================
print("=" * 60)
print("  VARIABLE EXPLORER")
print("=" * 60)

# Create different types and inspect them
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

# =============================================================================
# INTEGER CACHING — Python's Secret Optimization
# =============================================================================
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

print("\n" + "=" * 60)
