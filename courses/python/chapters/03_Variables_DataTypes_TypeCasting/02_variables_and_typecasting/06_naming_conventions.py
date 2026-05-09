"""
Naming Conventions and PEP 8
==============================
Run: python3 06_naming_conventions.py

Demonstrates:
- snake_case for variables and functions
- UPPER_SNAKE_CASE for constants
- PascalCase for classes
- Valid vs invalid variable names
- Reserved keywords
"""

import keyword

# =============================================================================
# PEP 8 NAMING CONVENTIONS
# =============================================================================
print("=" * 60)
print("  NAMING CONVENTIONS (PEP 8)")
print("=" * 60)

# Variables and functions: snake_case
user_name = "Vikram"
total_count = 42
is_active = True

print(f"\n--- Variables (snake_case) ---")
print(f"  user_name = '{user_name}'")
print(f"  total_count = {total_count}")
print(f"  is_active = {is_active}")

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
PI = 3.14159
DATABASE_URL = "localhost:5432"
API_TIMEOUT = 30

print(f"\n--- Constants (UPPER_SNAKE_CASE) ---")
print(f"  MAX_RETRIES = {MAX_RETRIES}")
print(f"  PI = {PI}")
print(f"  DATABASE_URL = '{DATABASE_URL}'")
print(f"  API_TIMEOUT = {API_TIMEOUT}")

# Classes: PascalCase (preview)
print(f"\n--- Classes (PascalCase) ---")
print(f"  class UserProfile:")
print(f"  class DatabaseConnection:")
print(f"  class HttpRequestHandler:")

# =============================================================================
# VALID VS INVALID NAMES
# =============================================================================
print("\n" + "=" * 60)
print("  VALID vs INVALID VARIABLE NAMES")
print("=" * 60)

print("\n--- Valid names ---")
valid_examples = [
    ("age", "starts with letter"),
    ("_private", "starts with underscore"),
    ("__dunder__", "double underscore (special)"),
    ("camelCase", "valid but not PEP 8 for variables"),
    ("x1", "letter followed by number"),
    ("data_2024", "underscores and numbers"),
]
for name, reason in valid_examples:
    print(f"  {name:<15} ({reason})")

print("\n--- Invalid names ---")
invalid_examples = [
    ("2fast", "cannot start with a number"),
    ("my-var", "hyphens not allowed"),
    ("my var", "spaces not allowed"),
    ("class", "reserved keyword"),
    ("@name", "special characters not allowed"),
]
for name, reason in invalid_examples:
    print(f"  {name:<15} ({reason})")

# =============================================================================
# PYTHON RESERVED KEYWORDS
# =============================================================================
print("\n" + "=" * 60)
print("  PYTHON RESERVED KEYWORDS")
print("=" * 60)

keywords = keyword.kwlist
print(f"\n  Total keywords: {len(keywords)}")
print(f"  Keywords:")

# Print in columns
cols = 5
for i in range(0, len(keywords), cols):
    row = keywords[i:i+cols]
    print("    " + "".join(f"{kw:<12}" for kw in row))

# Check if a word is a keyword
print(f"\n  keyword.iskeyword('for') = {keyword.iskeyword('for')}")
print(f"  keyword.iskeyword('hello') = {keyword.iskeyword('hello')}")

# =============================================================================
# NAMING BEST PRACTICES
# =============================================================================
print("\n" + "=" * 60)
print("  NAMING BEST PRACTICES")
print("=" * 60)

print("""
  DO:
    user_count = 42          # Descriptive, snake_case
    is_valid = True          # Boolean prefix: is_, has_, can_
    max_retries = 3          # Clear intent
    get_user_name()          # Function: verb + noun

  DON'T:
    x = 42                   # Too short (unless loop var)
    data = [...]             # Too generic
    myVar = "hello"          # camelCase (not Pythonic)
    VARIABLE = "not const"   # UPPER = constants only
""")

print("=" * 60)
