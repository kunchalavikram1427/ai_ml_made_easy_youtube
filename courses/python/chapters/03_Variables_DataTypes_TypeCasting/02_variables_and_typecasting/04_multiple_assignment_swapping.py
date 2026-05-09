"""
Multiple Assignment and Variable Swapping
===========================================
Run: python3 04_multiple_assignment_swapping.py

Demonstrates:
- Assigning the same value to multiple variables
- Tuple unpacking (multiple values in one line)
- Pythonic swap (no temp variable needed)
- Extended unpacking with * operator
"""

# =============================================================================
# SAME VALUE TO MULTIPLE VARIABLES
# =============================================================================
print("=" * 60)
print("  MULTIPLE ASSIGNMENT & SWAPPING")
print("=" * 60)

# Same value to multiple variables
x = y = z = 0
print(f"\nx = y = z = 0  ->  x={x}, y={y}, z={z}")
print(f"  All point to same object: {id(x) == id(y) == id(z)}")

# =============================================================================
# TUPLE UNPACKING (multiple values in one line)
# =============================================================================
print("\n--- Tuple Unpacking ---")

a, b, c = 10, 20, 30
print(f"a, b, c = 10, 20, 30  ->  a={a}, b={b}, c={c}")

# Works with lists too
x, y, z = [100, 200, 300]
print(f"x, y, z = [100, 200, 300]  ->  x={x}, y={y}, z={z}")

# Unpack from a function return
def get_coordinates():
    return 4.5, 7.2, 1.0

lat, lng, alt = get_coordinates()
print(f"lat, lng, alt = get_coordinates() -> {lat}, {lng}, {alt}")

# =============================================================================
# PYTHONIC SWAP (no temp variable!)
# =============================================================================
print("\n--- Pythonic Swap ---")

a, b = 10, 20
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After a, b = b, a: a={a}, b={b}")

# 3-way swap
x, y, z = 1, 2, 3
print(f"\nBefore: x={x}, y={y}, z={z}")
x, y, z = z, x, y
print(f"After x, y, z = z, x, y: x={x}, y={y}, z={z}")
