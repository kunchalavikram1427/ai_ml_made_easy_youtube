"""
String Creation, Indexing & Slicing
=====================================
Run: python3 01_string_creation_and_indexing.py

Covers:
- Creating strings with single, double, and triple quotes
- String indexing (positive and negative)
- String slicing with [start:stop:step]
- String immutability
- Escape characters and raw strings
- len() function
"""


# =============================================================================
# STRING CREATION
# =============================================================================

print("=" * 55)
print("  STRING CREATION")
print("=" * 55)

# Single quotes — most common
name = 'Vikram'
print(f"\n  Single quotes: '{name}'")

# Double quotes — useful when string contains single quotes
message = "It's a beautiful day"
print(f"  Double quotes: \"{message}\"")

# Triple quotes — multi-line strings
poem = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you!'''
print(f"\n  Triple quotes (multi-line):")
print(f"  {poem}")

# Empty string
empty = ""
print(f"\n  Empty string: '{empty}' (length: {len(empty)})")


# =============================================================================
# STRING INDEXING
# =============================================================================

print(f"\n{'=' * 55}")
print("  STRING INDEXING")
print("=" * 55)

text = "Python"
print(f"\n  text = '{text}'")
print(f"  Positive index:  P  y  t  h  o  n")
print(f"                   0  1  2  3  4  5")
print(f"  Negative index: -6 -5 -4 -3 -2 -1")

print(f"\n  text[0]  = '{text[0]}'")    # P (first character)
print(f"  text[1]  = '{text[1]}'")      # y
print(f"  text[-1] = '{text[-1]}'")     # n (last character)
print(f"  text[-2] = '{text[-2]}'")     # o (second from end)
print(f"  len(text) = {len(text)}")     # 6


# =============================================================================
# STRING SLICING [start:stop:step]
# =============================================================================

print(f"\n{'=' * 55}")
print("  STRING SLICING [start:stop:step]")
print("=" * 55)

text = "Hello, World!"
print(f"\n  text = '{text}'")

# Basic slicing
print(f"\n  text[0:5]   = '{text[0:5]}'")      # 'Hello' (stop is exclusive)
print(f"  text[7:12]  = '{text[7:12]}'")       # 'World'
print(f"  text[:5]    = '{text[:5]}'")          # 'Hello' (start defaults to 0)
print(f"  text[7:]    = '{text[7:]}'")          # 'World!' (stop defaults to end)
print(f"  text[:]     = '{text[:]}'")           # full copy

# Negative slicing
print(f"\n  text[-6:-1] = '{text[-6:-1]}'")     # 'World'
print(f"  text[-6:]   = '{text[-6:]}'")         # 'World!'

# Step
print(f"\n  text[::2]   = '{text[::2]}'")       # every 2nd character
print(f"  text[::3]   = '{text[::3]}'")         # every 3rd character
print(f"  text[::-1]  = '{text[::-1]}'")        # reversed string!

# Practical: check if palindrome
word = "racecar"
is_palindrome = word == word[::-1]
print(f"\n  '{word}' is palindrome? {is_palindrome}")


# =============================================================================
# STRING IMMUTABILITY
# =============================================================================

print(f"\n{'=' * 55}")
print("  STRING IMMUTABILITY")
print("=" * 55)

text = "Hello"
print(f"\n  text = '{text}'")
print(f"  Strings CANNOT be modified in place!")
print(f"  text[0] = 'J'  -> TypeError!")
print(f"\n  Instead, create a new string:")
new_text = "J" + text[1:]
print(f"  'J' + text[1:] = '{new_text}'")


# =============================================================================
# ESCAPE CHARACTERS & RAW STRINGS
# =============================================================================

print(f"\n{'=' * 55}")
print("  ESCAPE CHARACTERS")
print("=" * 55)

print(f"\n  \\n  = newline")
print(f"  \\t  = tab:\t<- here")
print(f"  \\\\  = backslash: \\")
print(f"  \\'  = single quote: '")
print(f"  \\\"  = double quote: \"")

# Raw strings (ignore escape characters)
print(f"\n  --- Raw Strings (prefix r) ---")
path = r"C:\Users\name\documents"
print(f"  r'C:\\Users\\name\\documents' = '{path}'")
print(f"  Useful for file paths and regex patterns!")

print(f"\n{'=' * 55}")
