"""
Input Validation
=================
Run: python3 04_input_validation.py

Demonstrates:
- Why validation is needed
- Basic try/except validation loop
- Range validation
- Yes/No confirmation pattern
- Menu selection pattern
"""

# =============================================================================
# WHY VALIDATION IS NEEDED
# =============================================================================
print("=" * 60)
print("  INPUT VALIDATION")
print("=" * 60)

print("""
  Users WILL enter unexpected data. Good programs handle
  this gracefully instead of crashing with errors.

  The core pattern:
    while True:
        try:
            value = int(input("..."))
            break  # valid — exit loop
        except ValueError:
            print("Try again!")
""")

# =============================================================================
# PATTERN 1: BASIC try/except LOOP
# =============================================================================
print("=" * 60)
print("  PATTERN 1: BASIC try/except LOOP")
print("=" * 60)

print("""
  while True:
      try:
          age = int(input("Enter your age: "))
          break  # Valid input, exit loop
      except ValueError:
          print("Please enter a valid number!")
""")

# Demonstrate with simulated inputs
print("--- Simulated demo ---")
test_inputs = ["abc", "hello", "25"]
print(f"  Simulated inputs: {test_inputs}\n")
for val in test_inputs:
    try:
        age = int(val)
        print(f"  Input '{val}' -> Valid! age = {age}")
    except ValueError:
        print(f"  Input '{val}' -> 'Please enter a valid number!'")

# =============================================================================
# PATTERN 2: RANGE VALIDATION
# =============================================================================
print("\n" + "=" * 60)
print("  PATTERN 2: RANGE VALIDATION")
print("=" * 60)

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

# Demonstrate with simulated inputs
print("--- Simulated demo ---")
test_inputs = ["abc", "-5", "150", "25"]
print(f"  Simulated inputs: {test_inputs}")
print(f"  Validating age (1-120):\n")
for val in test_inputs:
    try:
        age = int(val)
        if 1 <= age <= 120:
            print(f"  Input '{val}' -> VALID (age = {age})")
        else:
            print(f"  Input '{val}' -> REJECTED (out of range)")
    except ValueError:
        print(f"  Input '{val}' -> REJECTED (not a number)")

# =============================================================================
# PATTERN 3: YES/NO CONFIRMATION
# =============================================================================
print("\n" + "=" * 60)
print("  PATTERN 3: YES/NO CONFIRMATION")
print("=" * 60)

print("""
  while True:
      answer = input("Continue? (yes/no): ").lower().strip()
      if answer in ("yes", "y"):
          print("Continuing...")
          break
      elif answer in ("no", "n"):
          print("Exiting...")
          break
      else:
          print("Please enter 'yes' or 'no'")
""")

# Demonstrate with simulated inputs
print("--- Simulated demo ---")
test_inputs = ["maybe", "YES", "  y  ", "no"]
print(f"  Simulated inputs: {test_inputs}\n")
for val in test_inputs:
    cleaned = val.lower().strip()
    if cleaned in ("yes", "y"):
        print(f"  Input '{val}' -> cleaned to '{cleaned}' -> Accepted (yes)")
    elif cleaned in ("no", "n"):
        print(f"  Input '{val}' -> cleaned to '{cleaned}' -> Accepted (no)")
    else:
        print(f"  Input '{val}' -> cleaned to '{cleaned}' -> Invalid, ask again")

# =============================================================================
# PATTERN 4: MENU SELECTION
# =============================================================================
print("\n" + "=" * 60)
print("  PATTERN 4: MENU SELECTION")
print("=" * 60)

print("""
  menu = \"\"\"
  Choose an option:
    1. Add item
    2. Remove item
    3. View all
    4. Quit
  \"\"\"

  while True:
      print(menu)
      choice = input("Enter choice (1-4): ").strip()
      if choice == "1":
          print("Adding item...")
      elif choice == "2":
          print("Removing item...")
      elif choice == "3":
          print("Viewing all...")
      elif choice == "4":
          print("Goodbye!")
          break
      else:
          print("Invalid choice! Please enter 1-4.")
""")

# Demonstrate with simulated inputs
print("--- Simulated demo ---")
test_inputs = ["5", "abc", "1", "4"]
print(f"  Simulated inputs: {test_inputs}\n")
valid_choices = {"1": "Add item", "2": "Remove item", "3": "View all", "4": "Quit"}
for val in test_inputs:
    if val in valid_choices:
        print(f"  Input '{val}' -> Valid! Action: {valid_choices[val]}")
    else:
        print(f"  Input '{val}' -> Invalid choice! Please enter 1-4.")

# =============================================================================
# TRY IT YOURSELF (uncomment to run interactively)
# =============================================================================
# while True:
#     try:
#         age = int(input("Enter your age (1-120): "))
#         if 1 <= age <= 120:
#             break
#         else:
#             print("Age must be between 1 and 120!")
#     except ValueError:
#         print("Please enter a valid number!")
# print(f"Your age is {age}")
