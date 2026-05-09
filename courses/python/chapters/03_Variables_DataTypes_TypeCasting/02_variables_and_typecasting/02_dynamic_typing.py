"""
Dynamic Typing in Python
==========================
Run: python3 02_dynamic_typing.py

Demonstrates:
- Variables can change type at runtime
- Python is dynamically typed (no type declarations)
- Variables are just labels pointing to objects
"""

# =============================================================================
# DYNAMIC TYPING IN ACTION
# =============================================================================
print("=" * 60)
print("  DYNAMIC TYPING")
print("=" * 60)

# The same variable can hold different types
x = 42
print(f"\nx = {x}, type = {type(x)}")

x = "now I'm a string"
print(f"x = {x}, type = {type(x)}")

x = [1, 2, 3]
print(f"x = {x}, type = {type(x)}")

x = True
print(f"x = {x}, type = {type(x)}")

x = 3.14
print(f"x = {x}, type = {type(x)}")

x = {"name": "Vikram"}
print(f"x = {x}, type = {type(x)}")

# =============================================================================
# VARIABLES ARE LABELS, NOT BOXES
# =============================================================================
print("\n" + "=" * 60)
print("  VARIABLES ARE LABELS (not boxes)")
print("=" * 60)

# Multiple variables can point to the same object
a = [1, 2, 3]
b = a  # b is another label for the SAME list

print(f"\na = {a}")
print(f"b = {b}")
print(f"a is b: {a is b}")  # True — same object!
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

# Reassigning a label doesn't affect the object
a = "something else"
print(f"\nAfter a = 'something else':")
print(f"a = {a}")
print(f"b = {b}")  # b still points to [1, 2, 3]

print("\n" + "=" * 60)
