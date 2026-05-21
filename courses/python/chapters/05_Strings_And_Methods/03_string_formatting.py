"""
String Formatting
==================
Run: python3 03_string_formatting.py

Covers:
- f-strings (recommended — Python 3.6+)
- .format() method
- % formatting (old-style)
- Format specifications: width, alignment, precision
- Expressions inside f-strings
"""


# =============================================================================
# F-STRINGS (RECOMMENDED)
# =============================================================================

print("=" * 55)
print("  F-STRINGS (Python 3.6+)")
print("=" * 55)

name = "Vikram"
age = 28
city = "Hyderabad"

# Basic f-string
print(f"\n  f'Hello, {{name}}!' = f'Hello, {name}!'")
print(f"  f'Age: {{age}}'     = f'Age: {age}'")

# Expressions inside f-strings
print(f"\n  --- Expressions ---")
print(f"  f'2 + 3 = {{2 + 3}}'          = f'2 + 3 = {2 + 3}'")
print(f"  f'{{name.upper()}}'            = f'{name.upper()}'")

# Format specifications
print(f"\n  --- Number Formatting ---")
pi = 3.14159
price = 42.5
big_num = 1000000

print(f"  f'{{pi:.2f}}'       = '{pi:.2f}'")           # 2 decimal places
print(f"  f'{{pi:.4f}}'       = '{pi:.4f}'")           # 4 decimal places
print(f"  f'{{price:>10.2f}}' = '{price:>10.2f}'")     # right-aligned, 10 wide
print(f"  f'{{big_num:,}}'    = '{big_num:,}'")        # thousands separator
print(f"  f'{{big_num:_}}'    = '{big_num:_}'")        # underscore separator

# Padding and fill
text = "Hi"
print(f"\n  --- Padding ---")
print(f"  f'{{text:*>10}}' = '{text:*>10}'")   # right-align, fill with *
print(f"  f'{{text:*<10}}' = '{text:*<10}'")   # left-align
print(f"  f'{{text:*^10}}' = '{text:*^10}'")   # center


# =============================================================================
# .format() METHOD
# =============================================================================

print(f"\n{'=' * 55}")
print("  .format() METHOD")
print("=" * 55)

# Positional arguments
print("\n  --- Positional ---")
result = "Hello, {}! You are {} years old.".format(name, age)
print(f"  'Hello, {{}}! You are {{}} years old.'.format(name, age)")
print(f"  = '{result}'")

# Named arguments
result = "I live in {city} and work with {lang}".format(city="Hyderabad", lang="Python")
print(f"\n  --- Named ---")
print(f"  = '{result}'")

# Index-based
result = "{0} loves {1}. {1} is great!".format("Vikram", "Python")
print(f"\n  --- Indexed ---")
print(f"  '{{0}} loves {{1}}. {{1}} is great!'.format('Vikram', 'Python')")
print(f"  = '{result}'")