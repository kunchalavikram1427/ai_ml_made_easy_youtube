"""
The input() Function Basics
=============================
Run: python3 01_basic_input.py

Demonstrates:
- How input() works
- input() ALWAYS returns a string
- Using a prompt message
- input() with no prompt
"""

# =============================================================================
# HOW input() WORKS
# =============================================================================
print("=" * 60)
print("  THE input() FUNCTION")
print("=" * 60)

print("""
  Syntax: variable = input("prompt message")

  - Displays the prompt
  - Waits for user to type something and press Enter
  - Returns what they typed AS A STRING
""")

# =============================================================================
# input() ALWAYS RETURNS A STRING
# =============================================================================
print("=" * 60)
print("  input() ALWAYS RETURNS A STRING")
print("=" * 60)

print("\n(Simulated with hardcoded values for non-interactive demo)\n")

# Simulating what happens when user types different things
simulated_inputs = ["Vikram", "25", "3.14", "True"]
for val in simulated_inputs:
    print(f"  User types: {val:>8}  ->  type = {type(val)}  (always str!)")

print("\n  Key point: Even if user types a number, it's still a string!")
print("  '25' is NOT the same as 25")
print(f"  '25' + '25' = '{'25' + '25'}'  (string concatenation)")
print(f"  25 + 25 = {25 + 25}         (actual addition)")

# =============================================================================
# BASIC USAGE EXAMPLES
# =============================================================================
print("\n" + "=" * 60)
print("  BASIC USAGE EXAMPLES")
print("=" * 60)

print("""
  # With a prompt:
  name = input("What is your name? ")
  print(f"Hello, {name}!")

  # Without a prompt (just waits for input):
  data = input()

  # Prompt with no trailing space (cursor right after colon):
  age = input("Age:")

  # Prompt with trailing space (cursor has breathing room):
  age = input("Age: ")    # <-- prefer this style
""")

# =============================================================================
# KEY FACTS
# =============================================================================
print("=" * 60)
print("  KEY FACTS ABOUT input()")
print("=" * 60)

print("""
  1. ALWAYS returns a string (even if user types a number)
  2. Strips the trailing newline (you don't get \\n at the end)
  3. Blocks execution (program waits until user presses Enter)
  4. Prompt is optional (input() with no argument still works)
""")

# =============================================================================
# TRY IT YOURSELF (uncomment to run interactively)
# =============================================================================
# name = input("What is your name? ")
# print(f"Hello, {name}!")
# print(f"Your name is of type: {type(name)}")
