"""
Variable Scope — Local, Global, and the LEGB Rule
===================================================
Run: python3 07_variable_scope.py

Demonstrates:
- Local vs Global variables
- Variable shadowing
- The 'global' keyword
- The 'nonlocal' keyword (nested functions)
- LEGB rule: Local -> Enclosing -> Global -> Built-in
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
# LEGB RULE DEMONSTRATION
# =============================================================================
print("\n" + "-" * 60)
print("  LEGB RULE: Local -> Enclosing -> Global -> Built-in")
print("-" * 60)

x_scope = "global"

def outer_func():
    x_scope_e = "enclosing"

    def inner_func():
        x_scope_l = "local"
        print(f"\n  L (Local):    x_scope_l = '{x_scope_l}'")
        print(f"  E (Enclosing): x_scope_e = '{x_scope_e}'")
        print(f"  G (Global):   x_scope = '{x_scope}'")
        print(f"  B (Built-in): len = {len}")

    inner_func()

outer_func()

# Practical example of LEGB
print("\n--- Practical LEGB Example ---")

name = "Global Vikram"  # Global

def greet():
    name = "Local Vikram"  # Local shadows Global
    print(f"  Inside greet(): name = '{name}'")

greet()
print(f"  Outside greet(): name = '{name}'")

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

# del with lists
print("\n--- Deleting list elements ---")
my_list = [10, 20, 30, 40, 50]
print(f"Before: {my_list}")
del my_list[2]  # Remove element at index 2
print(f"After del my_list[2]: {my_list}")
del my_list[1:3]  # Remove slice
print(f"After del my_list[1:3]: {my_list}")

print("\n" + "=" * 60)
