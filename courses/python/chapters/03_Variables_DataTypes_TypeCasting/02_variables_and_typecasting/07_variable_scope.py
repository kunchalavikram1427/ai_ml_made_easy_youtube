"""
Variable Scope — Local, Global, and the LEGB Rule
===================================================
Run: python3 07_variable_scope.py

Demonstrates:
- Local vs Global variables
- Variable shadowing
- The 'global' keyword
- The 'nonlocal' keyword (nested functions)
- The 'del' keyword
"""

# =============================================================================
# LOCAL vs GLOBAL — SHADOWING
# =============================================================================
print("=" * 60)
print("  VARIABLE SCOPE (LEGB RULE)")
print("=" * 60)

threshold = 30  # Global variable

def monitor_temperature():
    threshold = 44  # Local — shadows the global
    print(f"  Inside function (local): threshold = {threshold}")

print(f"\nGlobal threshold: {threshold}")
monitor_temperature()
print(f"Global threshold after function call: {threshold}")  # Unchanged!

# =============================================================================
# THE 'global' KEYWORD
# =============================================================================
print("\n" + "-" * 60)
print("  THE 'global' KEYWORD")
print("-" * 60)

counter = 0

def increment():
    global counter
    counter += 1

print(f"\ncounter before: {counter}")
increment()
increment()
increment()
print(f"counter after 3 increments: {counter}")  # 3

# =============================================================================
# THE 'nonlocal' KEYWORD (nested functions)
# =============================================================================
print("\n" + "-" * 60)
print("  THE 'nonlocal' KEYWORD")
print("-" * 60)

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    print(f"\n  outer() -> inner() call 1: {inner()}")
    print(f"  outer() -> inner() call 2: {inner()}")
    print(f"  outer() -> inner() call 3: {inner()}")
    print(f"  outer() -> final count: {count}")

outer()


# =============================================================================
# THE 'del' KEYWORD
# =============================================================================
print("\n" + "=" * 60)
print("  THE 'del' KEYWORD")
print("=" * 60)

# del removes a variable reference
print("\n--- Deleting variables ---")
temp_var = 42
print(f"temp_var = {temp_var}")
del temp_var
try:
    print(temp_var)
except NameError as e:
    print(f"After 'del temp_var': {e}")