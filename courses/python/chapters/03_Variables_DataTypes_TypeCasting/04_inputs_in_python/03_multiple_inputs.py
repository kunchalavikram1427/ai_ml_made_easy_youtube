"""
Multiple Inputs on One Line
=============================
Run: python3 03_multiple_inputs.py

Demonstrates:
- Using .split() to break input into parts
- Using map() to convert multiple values at once
- Unpacking into variables
- Comma-separated input
- Collecting a list of numbers from one line
"""

# =============================================================================
# USING .split()
# =============================================================================
print("=" * 60)
print("  MULTIPLE INPUTS WITH .split()")
print("=" * 60)

print("\n--- Basic .split() ---")
user_input = "10 20 30"
parts = user_input.split()
print(f"  Input: '{user_input}'")
print(f"  .split() -> {parts}  (list of strings)")
print(f"  parts[0] = '{parts[0]}', type = {type(parts[0])}")

# =============================================================================
# USING map() TO CONVERT TYPES
# =============================================================================
print("\n" + "=" * 60)
print("  USING map() TO CONVERT ALL AT ONCE")
print("=" * 60)

print("\n--- map(int, ...) ---")
user_input = "10 20 30"
parts = user_input.split()
numbers = list(map(int, parts))
print(f"  Input: '{user_input}'")
print(f"  .split()         -> {parts}  (strings)")
print(f"  map(int, ...)    -> {numbers}  (integers!)")
print(f"  Sum: {sum(numbers)}")
print(f"  Average: {sum(numbers) / len(numbers):.2f}")

print("""
  How map() works:
    map(function, iterable)
    - Takes each item from the iterable
    - Applies the function to it
    - Returns the results
""")

# =============================================================================
# UNPACKING INTO VARIABLES
# =============================================================================
print("=" * 60)
print("  UNPACKING INTO VARIABLES")
print("=" * 60)

print("\n--- Two values ---")
user_input = "5 3"
x, y = map(int, user_input.split())
print(f"  Input: '{user_input}'")
print(f"  x, y = map(int, input().split())")
print(f"  x = {x}, y = {y}")
print(f"  x + y = {x + y}")
print(f"  x * y = {x * y}")

print("\n--- Three values ---")
user_input = "Alice 25 Hyderabad"
name, age, city = user_input.split()
age = int(age)
print(f"  Input: '{user_input}'")
print(f"  name = '{name}', age = {age}, city = '{city}'")

# =============================================================================
# COMMA-SEPARATED INPUT
# =============================================================================
print("\n" + "=" * 60)
print("  COMMA-SEPARATED INPUT")
print("=" * 60)

user_input = "python, ai, machine learning, data science"
tags = [tag.strip() for tag in user_input.split(",")]
print(f"  Input: '{user_input}'")
print(f"  .split(',') + strip -> {tags}")
print(f"  Number of tags: {len(tags)}")

# =============================================================================
# COLLECTING A LIST OF NUMBERS
# =============================================================================
print("\n" + "=" * 60)
print("  COLLECTING A LIST OF NUMBERS")
print("=" * 60)

print("""
  # Accept all numbers on one line:
  numbers = list(map(int, input("Enter numbers: ").split()))

  # Example: user types "5 10 15 20 25"
""")

user_input = "5 10 15 20 25"
numbers = list(map(int, user_input.split()))
print(f"  Input: '{user_input}'")
print(f"  Numbers: {numbers}")
print(f"  Sum: {sum(numbers)}")
print(f"  Min: {min(numbers)}")
print(f"  Max: {max(numbers)}")
print(f"  Average: {sum(numbers) / len(numbers):.1f}")

# =============================================================================
# TRY IT YOURSELF (uncomment to run interactively)
# =============================================================================
# a, b = map(int, input("Enter two integers (space-separated): ").split())
# print(f"{a} + {b} = {a + b}")
#
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print(f"Numbers: {numbers}, Sum: {sum(numbers)}")
