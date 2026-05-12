"""
Type Casting User Input
========================
Run: python3 02_type_casting_input.py

Demonstrates:
- Converting input strings to int and float
- Common casting patterns (strip, upper, lower)
- What happens when casting fails (ValueError)
- The one-liner pattern: int(input(...))
"""

# =============================================================================
# WHY WE NEED TYPE CASTING
# =============================================================================
print("=" * 60)
print("  TYPE CASTING USER INPUT")
print("=" * 60)

print("""
  Since input() ALWAYS returns a string, you must cast to
  the type you need before doing math or comparisons.
""")

# Demonstrate the problem
print("--- The problem without casting ---")
age_str = "25"
print(f"  age_str = '{age_str}'  (this is a string)")
print(f"  age_str + 5 would cause: TypeError!")
print(f"  We need: int('{age_str}') = {int(age_str)}")

# =============================================================================
# COMMON CASTING PATTERNS
# =============================================================================
print("\n" + "=" * 60)
print("  COMMON CASTING PATTERNS")
print("=" * 60)

print("\n--- String to int ---")
age_str = "25"
age_int = int(age_str)
print(f"  int('{age_str}') = {age_int}, type = {type(age_int)}")
print(f"  Now we can do math: {age_int} + 5 = {age_int + 5}")

print("\n--- String to float ---")
height_str = "1.75"
height_float = float(height_str)
print(f"  float('{height_str}') = {height_float}, type = {type(height_float)}")
print(f"  Formatted: {height_float:.2f}m")

print("\n--- Cleaning up input with .strip() and case methods ---")
user_input = "  Hello  "
print(f"  Input: '{user_input}'")
print(f"  .strip()  -> '{user_input.strip()}'")
print(f"  .upper()  -> '{user_input.strip().upper()}'")
print(f"  .lower()  -> '{user_input.strip().lower()}'")

# =============================================================================
# THE ONE-LINER PATTERN
# =============================================================================
print("\n" + "=" * 60)
print("  THE ONE-LINER PATTERN")
print("=" * 60)

print("""
  # Instead of two lines:
  age_str = input("Enter your age: ")
  age = int(age_str)

  # Use one line (very common in Python):
  age = int(input("Enter your age: "))
  height = float(input("Enter height (m): "))
  name = input("Name: ").strip()
  choice = input("Y/N: ").upper()
""")

# =============================================================================
# WHAT HAPPENS WHEN CASTING FAILS
# =============================================================================
print("=" * 60)
print("  WHAT HAPPENS WITH INVALID INPUT")
print("=" * 60)

print("\n  If user types something that can't be converted:\n")
invalid_inputs = ["hello", "", "3.14", "12abc"]
for val in invalid_inputs:
    try:
        result = int(val)
        print(f"  int('{val}') = {result}  (success)")
    except ValueError as e:
        print(f"  int('{val}') -> ValueError: {e}")

print("""
  This is why we need INPUT VALIDATION (see 04_input_validation.py)
""")

# =============================================================================
# TRY IT YOURSELF (uncomment to run interactively)
# =============================================================================
# age = int(input("Enter your age: "))
# print(f"In 5 years you'll be {age + 5}")
#
# height = float(input("Enter your height in meters: "))
# print(f"Height: {height:.2f}m")
