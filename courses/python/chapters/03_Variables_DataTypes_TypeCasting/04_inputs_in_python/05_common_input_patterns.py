"""
Common Input Patterns
======================
Run: python3 05_common_input_patterns.py

Demonstrates:
- Default values with 'or'
- Password input (hidden) with getpass
- Multi-line input (read until blank line)
- Smart type detection
"""

# =============================================================================
# DEFAULT VALUES PATTERN
# =============================================================================
print("=" * 60)
print("  DEFAULT VALUES PATTERN")
print("=" * 60)

print("""
  # If user just presses Enter, use a default:
  name = input("Name [Vikram]: ").strip() or "Vikram"
""")

print("--- How 'or' works for defaults ---\n")

# Simulated: user presses Enter without typing
user_input = ""
name = user_input.strip() or "Vikram"
print(f"  Input: '' (user pressed Enter)")
print(f"  Result: name = '{name}'  (default used)")

# Simulated: user types something
user_input = "Alice"
name = user_input.strip() or "Vikram"
print(f"\n  Input: 'Alice'")
print(f"  Result: name = '{name}'  (user value used)")

print("""
  Why this works:
    - Empty string '' is "falsy" in Python
    - '' or "Vikram" evaluates to "Vikram"
    - 'Alice' or "Vikram" evaluates to 'Alice'
""")

# =============================================================================
# PASSWORD INPUT (HIDDEN)
# =============================================================================
print("=" * 60)
print("  PASSWORD INPUT (HIDDEN)")
print("=" * 60)

print("""
  import getpass

  # Input is NOT shown on screen (no echo)
  password = getpass.getpass("Enter password: ")
  print(f"Password length: {len(password)}")

  Use cases:
  - Login prompts
  - API key entry
  - Any sensitive data
""")

# Can't demo getpass non-interactively, but show the concept
import getpass
print(f"  getpass module available: {hasattr(getpass, 'getpass')}")
print("  (Can't demo hidden input non-interactively)")

# =============================================================================
# MULTI-LINE INPUT
# =============================================================================
print("\n" + "=" * 60)
print("  MULTI-LINE INPUT")
print("=" * 60)

print("""
  # Read lines until user enters a blank line:
  print("Enter text (blank line to finish):")
  lines = []
  while True:
      line = input()
      if line == "":
          break
      lines.append(line)

  text = "\\n".join(lines)
""")

# Simulated demo
print("--- Simulated demo ---\n")
simulated_lines = ["Hello world", "This is line 2", "Final line", ""]
lines = []
for line in simulated_lines:
    if line == "":
        print(f"  > (blank line - stop)")
        break
    print(f"  > {line}")
    lines.append(line)

text = "\n".join(lines)
print(f"\n  Collected {len(lines)} lines:")
print(f"  '{text}'")

# =============================================================================
# SMART TYPE DETECTION
# =============================================================================
print("\n" + "=" * 60)
print("  SMART TYPE DETECTION")
print("=" * 60)

print("""
  Sometimes you want to auto-detect what the user meant:
  - "42" -> int
  - "3.14" -> float
  - "True" -> bool
  - "hello" -> str
""")


def smart_cast(value_string):
    """Auto-detect and cast a string to the appropriate type."""
    if value_string.lower() == "none":
        return None
    if value_string.lower() == "true":
        return True
    if value_string.lower() == "false":
        return False
    try:
        return int(value_string)
    except ValueError:
        pass
    try:
        return float(value_string)
    except ValueError:
        pass
    return value_string


# Test it
test_inputs = ["42", "3.14", "True", "False", "none", "hello", "-7", "0"]
print(f"\n  {'Input':>10} {'Value':>10} {'Type'}")
print(f"  {'-' * 40}")
for val in test_inputs:
    result = smart_cast(val)
    print(f"  {val:>10} {str(result):>10} {type(result).__name__}")

# =============================================================================
# TRY IT YOURSELF (uncomment to run interactively)
# =============================================================================
# name = input("Enter your name [Vikram]: ").strip() or "Vikram"
# print(f"Hello, {name}!")
#
# import getpass
# password = getpass.getpass("Enter password: ")
# print(f"Password length: {len(password)}")
#
# print("Enter text (blank line to finish):")
# lines = []
# while True:
#     line = input()
#     if line == "":
#         break
#     lines.append(line)
# print(f"You entered {len(lines)} lines")
