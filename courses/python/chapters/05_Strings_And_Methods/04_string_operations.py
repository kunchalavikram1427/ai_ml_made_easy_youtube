"""
String Operations — Concatenation, Repetition, Comparison & Encoding
=====================================================================
Run: python3 04_string_operations.py

Covers:
- Concatenation (+) and repetition (*)
- String comparison (lexicographic)
- String membership (in/not in)
"""


# =============================================================================
# CONCATENATION AND REPETITION
# =============================================================================

print("=" * 55)
print("  CONCATENATION & REPETITION")
print("=" * 55)

# Concatenation with +
first = "Hello"
second = "World"
combined = first + ", " + second + "!"
print(f"\n  '{first}' + ', ' + '{second}' + '!' = '{combined}'")


# Implicit concatenation (adjacent string literals)
message = ("This is a very long string "
           "that spans multiple lines "
           "in source code")
print(f"\n  Implicit concatenation:")
print(f"  '{message}'")

# Building strings efficiently with join
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"\n  ' '.join({words}) = '{sentence}'")
print(f"  (join is more efficient than + in loops)")


# =============================================================================
# STRING COMPARISON
# =============================================================================

print(f"\n{'=' * 55}")
print("  STRING COMPARISON")
print("=" * 55)

# Case-insensitive comparison
print(f"\n  --- Case-Insensitive ---")
s1 = "Hello"
s2 = "hello"
print(f"  '{s1}' == '{s2}'            -> {s1 == s2}")           # False
print(f"  '{s1}'.lower() == '{s2}'.lower() -> {s1.lower() == s2.lower()}")  # True

# Unicode values
'''
Computers do not understand letters, emojis, or symbols; they only understand numbers. 
Unicode is the universal standard that assigns a unique number (called a code point) to every character in the world.
Python uses ord() and chr() as inverse functions to translate between these characters and their numerical values

ord(character) (Ordinal): Takes a single character string and returns its integer Unicode value.
chr(integer) (Character): Takes an integer Unicode value and returns its corresponding character string.

Visit: http://unicodeplus.com
'''

print(f"\n  --- Unicode Values (ord/chr) ---")
print(f"  ord('A') = {ord('A')}")     # 65
print(f"  ord('a') = {ord('a')}")     # 97
print(f"  ord('0') = {ord('0')}")     # 48
print(f"  chr(65)  = '{chr(65)}'")    # 'A'
print(f"  chr(97)  = '{chr(97)}'")    # 'a'

char = 'G'
print(f"\n  Character: '{char}'")
# Check if it is an uppercase letter (65 to 90)
if 65 <= ord(char) <= 90:
    print(f"'{char}' is an uppercase letter.")


print(f"\n  --- Printing Unicode characters. ---")

print(f"---Using 4-digit Hex with---")
print(f" 00A3 = {'\u00A3'}")  # Output: £ (Pound sign)
print(f" 03B1 = {'\u03B1'}")  # Output: α (Greek alpha)
print(f" 1F44D = {'\U0001F44D'}")  # Output: 👍 (Thumbs up); http://unicodeplus.com/U+1F44D

print(f"---Using 8-digit Hex with---")
print(f" 0001F600 = {'\U0001F600'}")  # Output: 😀 (Grinning face emoji)

print(f"---Using the `chr()` Function---")
# The `chr()` function converts a Unicode code point (integer) into its corresponding character.
print(f" chr(8364) = '{chr(8364)}'")  # Using Decimal (Base 10). Output: € (Euro sign)
print(f" chr(0x2112) = '{chr(0x2112)}'")  # Using Hexadecimal (Base 16). Output: ℒ (Script capital L)

print(f"---Using the  official Unicode character name---")
print(f"  GREEK CAPITAL LETTER DELTA =   \N{GREEK CAPITAL LETTER DELTA}")  # Output: Δ
print(f"  THUMBS UP SIGN = \N{THUMBS UP SIGN}")              # Output: 👍
print(f"  SPARKLES = \N{SPARKLES}")                   # Output: ✨


# =============================================================================
# MEMBERSHIP (in / not in)
# =============================================================================

print(f"\n{'=' * 55}")
print("  STRING MEMBERSHIP")
print("=" * 55)

text = "Hello, World! Welcome to Python"
print(f"\n  text = '{text}'")
print(f"  'World' in text     -> {'World' in text}")       # True
print(f"  'world' in text     -> {'world' in text}")       # False (case-sensitive)
print(f"  'Python' in text    -> {'Python' in text}")      # True
print(f"  'Java' not in text  -> {'Java' not in text}")    # True