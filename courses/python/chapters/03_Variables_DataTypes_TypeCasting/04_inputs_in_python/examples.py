"""
Inputs in Python - Examples
============================
Run: python3 examples.py

This script demonstrates:
- input() function basics
- Type casting user input
- Multiple inputs on one line
- Input validation patterns
- sys.stdin usage
- Building interactive programs

Note: Some sections are shown as non-interactive demos.
      Uncomment the interactive sections to try them yourself.
"""

import sys

# =============================================================================
# SECTION 1: BASIC input() FUNCTION
# =============================================================================
print("=" * 60)
print("  BASIC input() FUNCTION")
print("=" * 60)

# Demonstrate that input() always returns a string
print("\n--- input() always returns a string ---")
print("(Simulated with hardcoded values for non-interactive demo)\n")

# Simulating what happens when user types different things
simulated_inputs = ["Vikram", "25", "3.14", "True"]
for val in simulated_inputs:
    print(f"  User types: {val:>8}  ->  type = {type(val)}  (always str!)")

print("\n  To use as a number, you MUST cast:")
age_str = "25"
age_int = int(age_str)
print(f"  int('{age_str}') = {age_int}, type = {type(age_int)}")
print(f"  Now we can do math: {age_int} + 5 = {age_int + 5}")


# =============================================================================
# SECTION 2: TYPE CASTING INPUT
# =============================================================================
print("\n" + "=" * 60)
print("  TYPE CASTING INPUT")
print("=" * 60)

# Simulated input conversions
print("\n--- Common casting patterns ---")
print("  age = int(input('Age: '))              # String -> int")
print("  height = float(input('Height: '))      # String -> float")
print("  name = input('Name: ').strip()         # Remove whitespace")
print("  choice = input('Y/N: ').upper()        # Normalize case")

# What happens when casting fails
print("\n--- What happens with invalid input ---")
invalid_inputs = ["hello", "", "3.14", "12abc"]
for val in invalid_inputs:
    try:
        result = int(val)
        print(f"  int('{val}') = {result}")
    except ValueError as e:
        print(f"  int('{val}') -> ValueError: {e}")


# =============================================================================
# SECTION 3: MULTIPLE INPUTS ON ONE LINE
# =============================================================================
print("\n" + "=" * 60)
print("  MULTIPLE INPUTS ON ONE LINE")
print("=" * 60)

# Demonstrate split() and map()
print("\n--- Using .split() ---")
user_input = "10 20 30"
parts = user_input.split()
print(f"  Input: '{user_input}'")
print(f"  .split() -> {parts}  (list of strings)")

# Convert to integers
numbers = list(map(int, parts))
print(f"  map(int, ...) -> {numbers}  (list of ints)")
print(f"  Sum: {sum(numbers)}")

# Unpacking into variables
print("\n--- Unpacking into variables ---")
user_input = "5 3"
x, y = map(int, user_input.split())
print(f"  Input: '{user_input}'")
print(f"  x = {x}, y = {y}")
print(f"  x + y = {x + y}")
print(f"  x * y = {x * y}")

# Comma-separated input
print("\n--- Comma-separated values ---")
user_input = "python, ai, machine learning, data science"
tags = [tag.strip() for tag in user_input.split(",")]
print(f"  Input: '{user_input}'")
print(f"  Tags: {tags}")


# =============================================================================
# SECTION 4: INPUT VALIDATION PATTERNS
# =============================================================================
print("\n" + "=" * 60)
print("  INPUT VALIDATION PATTERNS")
print("=" * 60)

print("\n--- Pattern 1: Basic try/except loop ---")
print("""
  while True:
      try:
          age = int(input("Enter your age: "))
          break  # Valid input, exit loop
      except ValueError:
          print("Please enter a valid number!")
""")

print("--- Pattern 2: Range validation ---")
print("""
  while True:
      try:
          age = int(input("Age (1-120): "))
          if 1 <= age <= 120:
              break
          print("Must be between 1 and 120!")
      except ValueError:
          print("Please enter a valid number!")
""")

print("--- Pattern 3: Yes/No confirmation ---")
print("""
  while True:
      answer = input("Continue? (yes/no): ").lower().strip()
      if answer in ("yes", "y"):
          break
      elif answer in ("no", "n"):
          break
      print("Please enter 'yes' or 'no'")
""")

# Demonstrate validation with simulated inputs
print("--- Validation demo (simulated) ---")
test_inputs = ["abc", "-5", "150", "25"]
print(f"  Simulated inputs: {test_inputs}")
print(f"  Validating age (1-120):")
for val in test_inputs:
    try:
        age = int(val)
        if 1 <= age <= 120:
            print(f"    '{val}' -> VALID (age = {age})")
        else:
            print(f"    '{val}' -> REJECTED (out of range)")
    except ValueError:
        print(f"    '{val}' -> REJECTED (not a number)")


# =============================================================================
# SECTION 5: DEFAULT VALUES PATTERN
# =============================================================================
print("\n" + "=" * 60)
print("  DEFAULT VALUES PATTERN")
print("=" * 60)

# Using 'or' for defaults
print("\n--- Using 'or' for defaults ---")
user_input = ""  # Simulates user pressing Enter without typing
name = user_input.strip() or "Vikram"
print(f"  Input: '' (empty)")
print(f"  name = input(...).strip() or 'Vikram'")
print(f"  Result: name = '{name}'")

user_input = "Alice"
name = user_input.strip() or "Vikram"
print(f"\n  Input: 'Alice'")
print(f"  Result: name = '{name}'")


# =============================================================================
# SECTION 6: sys.stdin FOR PIPED INPUT
# =============================================================================
print("\n" + "=" * 60)
print("  sys.stdin FOR PIPED INPUT")
print("=" * 60)

print("""
  Usage: echo "hello world" | python3 script.py
  Or:    cat data.txt | python3 script.py

  Code:
    import sys
    for line in sys.stdin:
        print(line.strip().upper())

  sys.stdout.write() — no auto-newline:
    sys.stdout.write("Hello\\n")  # Must add \\n yourself
""")

# Demonstrate sys.stdout.write
print("--- sys.stdout.write() demo ---")
sys.stdout.write("  This uses sys.stdout.write()")
sys.stdout.write(" — no newline added!\n")


# =============================================================================
# SECTION 7: SMART CAST FUNCTION
# =============================================================================
print("\n" + "=" * 60)
print("  SMART CAST — AUTO-DETECT INPUT TYPE")
print("=" * 60)


def smart_cast(value_string):
    """Auto-detect and cast a string to the appropriate type."""
    # Check for None
    if value_string.lower() == "none":
        return None

    # Check for boolean
    if value_string.lower() == "true":
        return True
    if value_string.lower() == "false":
        return False

    # Try int
    try:
        return int(value_string)
    except ValueError:
        pass

    # Try float
    try:
        return float(value_string)
    except ValueError:
        pass

    # Default: return as string
    return value_string


# Test the smart_cast function
test_inputs = ["42", "3.14", "True", "False", "none", "hello", "-7", "0"]
print(f"\n{'Input':>10} {'Value':>10} {'Type'}")
print("-" * 45)
for val in test_inputs:
    result = smart_cast(val)
    print(f"{val:>10} {str(result):>10} {type(result).__name__}")


# =============================================================================
# SECTION 8: INTERACTIVE PROGRAM EXAMPLE
# =============================================================================
print("\n" + "=" * 60)
print("  INTERACTIVE CALCULATOR (code shown, not executed)")
print("=" * 60)

print("""
def calculator():
    print("=== Simple Calculator ===")
    print("Type 'quit' to exit\\n")

    while True:
        expression = input("Enter (e.g., 5 + 3): ").strip()

        if expression.lower() == "quit":
            print("Goodbye!")
            break

        try:
            parts = expression.split()
            num1, op, num2 = float(parts[0]), parts[1], float(parts[2])

            if op == "+": result = num1 + num2
            elif op == "-": result = num1 - num2
            elif op == "*": result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print(f"Unknown operator: {op}")
                continue

            print(f"  = {result}")
        except (ValueError, IndexError):
            print("Format: number operator number")

# Uncomment to run interactively:
# calculator()
""")

print("=" * 60)
print("  END OF INPUTS TUTORIAL")
print("=" * 60)
print("\nTo try the interactive examples, uncomment them and run again!")
