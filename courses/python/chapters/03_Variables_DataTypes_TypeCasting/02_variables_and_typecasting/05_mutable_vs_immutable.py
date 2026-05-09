"""
Mutable vs Immutable Types
============================
Run: python3 05_mutable_vs_immutable.py

Demonstrates:
- Immutable types: int, float, str, tuple (new object on change)
- Mutable types: list, dict, set (modify in place)
- Aliasing trap (two variables, same object)
- Safe copying with .copy() and slicing
"""

# =============================================================================
# IMMUTABLE: Changing value creates a NEW object
# =============================================================================
print("=" * 60)
print("  MUTABLE vs IMMUTABLE")
print("=" * 60)

print("\n--- Immutable (int) ---")
x = 10
print(f"x = 10, id(x) = {id(x)}")
x = x + 1
print(f"x = x + 1 -> x = {x}, id(x) = {id(x)}  (NEW object!)")

print("\n--- Immutable (string) ---")
s = "hello"
print(f"s = 'hello', id(s) = {id(s)}")
s = s + " world"
print(f"s = s + ' world' -> s = '{s}', id(s) = {id(s)}  (NEW object!)")

print("\n--- Immutable (tuple) ---")
t = (1, 2, 3)
print(f"t = (1, 2, 3), id(t) = {id(t)}")
t = t + (4,)
print(f"t = t + (4,) -> t = {t}, id(t) = {id(t)}  (NEW object!)")

# =============================================================================
# MUTABLE: Modifying in place keeps the SAME object
# =============================================================================
print("\n--- Mutable (list) ---")
my_list = [1, 2, 3]
print(f"my_list = {my_list}, id = {id(my_list)}")
my_list.append(4)
print(f"my_list.append(4) -> {my_list}, id = {id(my_list)}  (SAME object!)")

print("\n--- Mutable (dict) ---")
my_dict = {"name": "Vikram"}
print(f"my_dict = {my_dict}, id = {id(my_dict)}")
my_dict["age"] = 25
print(f"my_dict['age'] = 25 -> {my_dict}, id = {id(my_dict)}  (SAME object!)")

print("\n--- Mutable (set) ---")
my_set = {1, 2, 3}
print(f"my_set = {my_set}, id = {id(my_set)}")
my_set.add(4)
print(f"my_set.add(4) -> {my_set}, id = {id(my_set)}  (SAME object!)")

# =============================================================================
# THE ALIASING TRAP
# =============================================================================
print("\n" + "=" * 60)
print("  THE ALIASING TRAP")
print("=" * 60)

print("\n--- The problem ---")
a = [1, 2, 3]
b = a  # b points to the SAME list!
b.append(99)
print(f"a = {a}")  # a is also affected!
print(f"b = {b}")
print(f"a is b: {a is b}")  # True!
print("  -> Modifying b also modified a! (same object)")

# =============================================================================
# SAFE COPYING
# =============================================================================
print("\n--- Safe copying (independent copies) ---")

# Method 1: .copy()
a = [1, 2, 3]
c = a.copy()
c.append(99)
print(f"\nUsing .copy():")
print(f"  a = {a}")  # Unaffected!
print(f"  c = {c}")
print(f"  a is c: {a is c}")  # False

# Method 2: slice [:]
a = [1, 2, 3]
d = a[:]
d.append(99)
print(f"\nUsing slice [:]:")
print(f"  a = {a}")  # Unaffected!
print(f"  d = {d}")

# Method 3: list() constructor
a = [1, 2, 3]
e = list(a)
e.append(99)
print(f"\nUsing list():")
print(f"  a = {a}")  # Unaffected!
print(f"  e = {e}")

# WARNING: Shallow copy only!
print("\n--- WARNING: Shallow copy doesn't copy nested objects ---")
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0].append(99)
print(f"  nested = {nested}")  # Inner list affected!
print(f"  shallow = {shallow}")
print("  -> Use copy.deepcopy() for nested structures!")

# Deep copy
import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
deep[0].append(99)
print(f"\n  Using deepcopy:")
print(f"  nested = {nested}")  # Unaffected!
print(f"  deep = {deep}")

print("\n" + "=" * 60)
