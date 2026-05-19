"""
String Operations — Concatenation, Repetition, Comparison & Encoding
=====================================================================
Run: python3 04_string_operations.py

Covers:
- Concatenation (+) and repetition (*)
- String comparison (lexicographic)
- String membership (in/not in)
- Multi-line strings and line handling
- encode() and decode() basics
- Common string patterns and recipes
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

# Repetition with *
line = "-" * 40
print(f"  '-' * 40 = '{line}'")
border = "=-" * 20 + "="
print(f"  '=-' * 20 + '=' = '{border}'")

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

# Lexicographic comparison (character by character using Unicode)
print(f"\n  --- Lexicographic Order ---")
print(f"  'apple' < 'banana'  -> {'apple' < 'banana'}")    # True (a < b)
print(f"  'apple' < 'Apple'   -> {'apple' < 'Apple'}")     # False (a=97, A=65)
print(f"  'abc' == 'abc'      -> {'abc' == 'abc'}")        # True
print(f"  'abc' < 'abd'       -> {'abc' < 'abd'}")         # True (c < d)
print(f"  'cat' < 'catalog'   -> {'cat' < 'catalog'}")     # True (shorter prefix)

# Case-insensitive comparison
print(f"\n  --- Case-Insensitive ---")
s1 = "Hello"
s2 = "hello"
print(f"  '{s1}' == '{s2}'            -> {s1 == s2}")           # False
print(f"  '{s1}'.lower() == '{s2}'.lower() -> {s1.lower() == s2.lower()}")  # True

# Unicode values
print(f"\n  --- Unicode Values (ord/chr) ---")
print(f"  ord('A') = {ord('A')}")     # 65
print(f"  ord('a') = {ord('a')}")     # 97
print(f"  ord('0') = {ord('0')}")     # 48
print(f"  chr(65)  = '{chr(65)}'")    # 'A'
print(f"  chr(97)  = '{chr(97)}'")    # 'a'


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


# =============================================================================
# MULTI-LINE STRINGS AND LINE HANDLING
# =============================================================================

print(f"\n{'=' * 55}")
print("  MULTI-LINE STRINGS")
print("=" * 55)

# splitlines()
text = "Line 1\nLine 2\nLine 3"
lines = text.splitlines()
print(f"\n  text = 'Line 1\\nLine 2\\nLine 3'")
print(f"  text.splitlines() = {lines}")

# Count lines, words, characters
paragraph = """Python is a programming language.
It is easy to learn.
Many people love Python."""

line_count = len(paragraph.splitlines())
word_count = len(paragraph.split())
char_count = len(paragraph)
print(f"\n  Paragraph analysis:")
print(f"    Lines:      {line_count}")
print(f"    Words:      {word_count}")
print(f"    Characters: {char_count}")


# =============================================================================
# ENCODE AND DECODE
# =============================================================================

print(f"\n{'=' * 55}")
print("  ENCODE & DECODE")
print("=" * 55)

text = "Hello"
encoded = text.encode("utf-8")
print(f"\n  '{text}'.encode('utf-8') = {encoded}")
print(f"  type = {type(encoded)}")

decoded = encoded.decode("utf-8")
print(f"  {encoded}.decode('utf-8') = '{decoded}'")

# Unicode text
hindi = "namaste"
encoded_hindi = hindi.encode("utf-8")
print(f"\n  '{hindi}'.encode('utf-8') = {encoded_hindi}")
print(f"  Length in chars: {len(hindi)}, in bytes: {len(encoded_hindi)}")


# =============================================================================
# COMMON RECIPES
# =============================================================================

print(f"\n{'=' * 55}")
print("  COMMON STRING RECIPES")
print("=" * 55)

# Reverse a string
text = "Python"
print(f"\n  Reverse '{text}': '{text[::-1]}'")

# Remove all whitespace
messy = "  H e l l o  "
clean = messy.replace(" ", "")
print(f"  Remove spaces from '{messy}': '{clean}'")

# Title case with exceptions
text = "the quick brown fox"
print(f"  Title case: '{text.title()}'")

# Check if string contains only ASCII
text = "Hello123"
print(f"  '{text}'.isascii() = {text.isascii()}")

# Repeat pattern
pattern = "ab" * 5
print(f"  'ab' * 5 = '{pattern}'")

print(f"\n{'=' * 55}")
