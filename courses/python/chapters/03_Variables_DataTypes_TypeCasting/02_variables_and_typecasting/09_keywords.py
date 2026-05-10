"""
Python 'keyword' Module — Listing All Reserved Keywords
========================================================
Run: python3 08_keywords.py

Demonstrates:
- Importing the built-in 'keyword' module
- Listing all Python reserved keywords
- Counting total number of keywords
- Understanding keyword immutability (cannot be used as identifiers)
"""

# =============================================================================
# IMPORTING THE 'keyword' MODULE
# =============================================================================
print("=" * 60)
print("  PYTHON KEYWORD MODULE")
print("=" * 60)

import keyword  # Built-in module to work with Python keywords

# =============================================================================
# LIST ALL KEYWORDS
# =============================================================================
print("\n" + "-" * 60)
print("  LIST OF PYTHON KEYWORDS")
print("-" * 60)

print("\nAll Python Keywords:")
print(keyword.kwlist)  # Returns list of all reserved keywords

# =============================================================================
# COUNT TOTAL KEYWORDS
# =============================================================================
print("\n" + "-" * 60)
print("  TOTAL KEYWORD COUNT")
print("-" * 60)

print(f"\nTotal number of keywords: {len(keyword.kwlist)}")

# =============================================================================
# CHECK IF A WORD IS A KEYWORD
# =============================================================================
print("\n" + "-" * 60)
print("  CHECKING KEYWORDS")
print("-" * 60)

test_words = ["for", "vikram", "class", "deploy"]

for word in test_words:
    print(f"Is '{word}' a keyword? -> {keyword.iskeyword(word)}")

# =============================================================================
# KEYWORDS CANNOT BE USED AS VARIABLE NAMES
# =============================================================================
print("\n" + "=" * 60)
print("  KEYWORDS AS IDENTIFIERS (INVALID USAGE)")
print("=" * 60)

print("\n--- Attempting to use a keyword as a variable ---")

try:
    exec("for = 10")  # This will raise SyntaxError
except SyntaxError as e:
    print(f"Error: Cannot use keyword as variable name -> {e}")