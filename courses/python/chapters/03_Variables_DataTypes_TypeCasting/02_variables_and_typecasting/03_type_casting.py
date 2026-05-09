"""
Type Casting — Converting Between Types
=========================================
Run: python3 03_type_casting.py

Demonstrates:
- Implicit type conversion (coercion)
- Explicit casting: int(), float(), str(), bool()
- Hex, binary, and octal conversions
- Truthy and Falsy values
- Safe casting with error handling
"""

# =============================================================================
# IMPLICIT TYPE CONVERSION (Python does it automatically)
# =============================================================================
print("=" * 60)
print("  IMPLICIT TYPE CONVERSION (Coercion)")
print("=" * 60)

result = 5 + 3.2  # int + float -> float
print(f"\n5 + 3.2 = {result} (type: {type(result).__name__})")

result2 = True + True + False  # bool in arithmetic: True=1, False=0
print(f"True + True + False = {result2} (type: {type(result2).__name__})")

result3 = 10 * True  # int * bool
print(f"10 * True = {result3} (type: {type(result3).__name__})")

result4 = 3 + 4j + 2  # int + complex -> complex
print(f"3 + 4j + 2 = {result4} (type: {type(result4).__name__})")

# =============================================================================
# int() CONVERSIONS
# =============================================================================
print("\n" + "=" * 60)
print("  int() CONVERSIONS")
print("=" * 60)

print(f"\nint(3.9) = {int(3.9)}")         # Truncates (not rounds!)
print(f"int(-3.9) = {int(-3.9)}")         # Truncates toward zero
print(f"int('42') = {int('42')}")
print(f"int('FF', 16) = {int('FF', 16)}")     # Hex to int
print(f"int('1010', 2) = {int('1010', 2)}")   # Binary to int
print(f"int('77', 8) = {int('77', 8)}")       # Octal to int
print(f"int(True) = {int(True)}")
print(f"int(False) = {int(False)}")

# =============================================================================
# float() CONVERSIONS
# =============================================================================
print("\n" + "=" * 60)
print("  float() CONVERSIONS")
print("=" * 60)

print(f"\nfloat(42) = {float(42)}")
print(f"float('3.14') = {float('3.14')}")
print(f"float('inf') = {float('inf')}")
print(f"float('-inf') = {float('-inf')}")
print(f"float('nan') = {float('nan')}")
print(f"float(True) = {float(True)}")

# =============================================================================
# str() CONVERSIONS
# =============================================================================
print("\n" + "=" * 60)
print("  str() CONVERSIONS")
print("=" * 60)

print(f"\nstr(42) = '{str(42)}'")
print(f"str(3.14) = '{str(3.14)}'")
print(f"str(True) = '{str(True)}'")
print(f"str(None) = '{str(None)}'")
print(f"str([1,2,3]) = '{str([1,2,3])}'")
print(f"str({{'a': 1}}) = '{str({'a': 1})}'")

# =============================================================================
# bool() CONVERSIONS — Truthy and Falsy
# =============================================================================
print("\n" + "=" * 60)
print("  bool() — TRUTHY AND FALSY VALUES")
print("=" * 60)

print("\nFalsy values (evaluate to False):")
falsy_values = [0, 0.0, "", [], {}, (), set(), None, False]
for val in falsy_values:
    print(f"  bool({repr(val):>10}) = {bool(val)}")

print("\nTruthy values (evaluate to True):")
truthy_values = [1, -1, 3.14, "hello", [0], {"a": 1}, (0,), True]
for val in truthy_values:
    print(f"  bool({repr(val):>10}) = {bool(val)}")

# =============================================================================
# SAFE CASTING WITH ERROR HANDLING
# =============================================================================
print("\n" + "=" * 60)
print("  SAFE CASTING (with error handling)")
print("=" * 60)

print("\nAttempting int() on various strings:")
test_values = ["42", "3.14", "hello", "", "True", "0xFF", "  7  "]
for val in test_values:
    try:
        result = int(val)
        print(f"  int('{val}') = {result}")
    except ValueError:
        print(f"  int('{val}') -> ValueError! Cannot convert.")

print("\n" + "=" * 60)
